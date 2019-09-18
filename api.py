# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

from steps import StepsFactory

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']
    factory = StepsFactory()
    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        
        step = factory.getStep('intro')

        sessionStorage[user_id] = {
            'answers': {},
            'last_question': step.getName()
        }

        userMessage = req['request']['original_utterance'].lower()

        res['response']['text'] = step.getText()
        return
    
    # Обрабатываем ответ пользователя.

    step = factory.getStep(sessionStorage[user_id]['last_question'])
    userMessage = req['request']['original_utterance'].lower()
    step.saveAnswer(sessionStorage[user_id], userMessage)
    
    if step.getName() == 'suggest':
        res['response']['text'] = step.getResult(sessionStorage[user_id])
        return
    
    nextStep = step.getNextStep()
    sessionStorage[user_id]['last_question'] = nextStep.getName()
    res['response']['text'] = nextStep.getText()