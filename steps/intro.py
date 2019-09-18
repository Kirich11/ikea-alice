from .hardness import Hardness
import random

class Intro:
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

    def getName (self) :
        return self.name
    
    def getText (self) :
        messageIndex = random.randint(0,3)
        helloIndex = random.randint(0,1)
        return self.hello[helloIndex] + ", " + self.dictionary[messageIndex]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['size'] = userMessage

    def getNextStep (self) :
        return Hardness()