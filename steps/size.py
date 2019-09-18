from .hardness import Hardness
import random

class Size:
    def __init__ (self) :
        self.dictionary = [
            'я помогу подобрать матрас.\r\n',
            'ответьте на несколько вопросов, чтобы я подобрала вам матрас.\r\n',
            'помогу вам выбрать комфортный матрас.\r\n',
            'давайте уточним некоторые детали.\r\n'
        ]
        self.question = [
            'Какой ширины матрас вам нужен?'
        ]
        self.hello = ['Привет']
        self.name = 'size'
        self.nextStep = Hardness()

    def getName (self) :
        return self.name
    
    def getText (self, previousAnswer = '') :
        if previousAnswer == '':
            messageIndex = random.randint(0,3)
            # helloIndex = random.randint(0,1)
            # questionIndex = random.randint(0,1)
            return self.hello[0] + ", " + self.dictionary[messageIndex] + self.question[0]
        if previousAnswer == 0:
            self.nextStep = Size()
            return "Вы не дали мне ширину матраса. Пожалуйста, скажите какой ширины матрас нужен вам?"

    def saveAnswer(self, userSession, userMessage):
        entities = userMessage['nlu']['entities']
        width = 0
        isNum = False
        for k in entities :
            if k['type'] == "YANDEX.NUMBER":
                if not isNum :
                    width = k['value']
                    isNum = True
        userSession['answers']['size'] = width
        if width == 0 :
            self.nextStep = Size()
        

    def getNextStep (self) :
        return self.nextStep