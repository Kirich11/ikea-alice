from .hardness import Hardness
import random

class Size:
    def __init__ (self) :
        self.dictionary = [
            'я помогу подобрать матрас, мне нужна ваша помощь.\r\n',
            'ответьте на несколько вопросов, чтобы я подобрала вам матрас.\r\n',
            'помогу вам выбрать комфортный матрас.\r\n',
            'давайте уточним некоторые детали.\r\n'
        ]
        self.question = [
            'Скажите какой ширины матрас нужен вам.',
            'Какой ширины матрас нужен вам?'
        ]
        self.hello = ['Хорошо', 'Привет']
        self.name = 'intro'
        self.nextStep = Hardness()

    def getName (self) :
        return self.name
    
    def getText (self, previousAnswer = '') :
        if previousAnswer == '':
            messageIndex = random.randint(0,3)
            helloIndex = random.randint(0,1)
            questionIndex = random.randint(0,1)
            return self.hello[helloIndex] + ", " + self.dictionary[messageIndex] + self.question[questionIndex]
        if previousAnswer == 0:
            self.nextStep = Size()
            return "Вы не дали мне ширину матраса. Пожалуйста, скажите какой ширины матрас нужен вам?"

    def saveAnswer(self, userSession, userMessage):
        entities = userMessage['nlu']['entities']
        width = 0
        for k in entities :
            if k['type'] == "YANDEX.NUMBER":
                width = k['value']
                userSession['answers']['intro'] = width
        if width == 0 :
            self.nextStep = Size()
        

    def getNextStep (self) :
        return self.nextStep