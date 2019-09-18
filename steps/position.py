from .temperature import Temperature
import random

class Position:
    def __init__ (self) :
        self.dictionary = [
            'В каком положении вы спите?',
            'В какой позе вам удобней спать?'
        ]
        self.name = 'position'

    def getName (self) :
        return self.name

    def getText (self) :
        index = random.randint(0,1)
        return self.dictionary[index]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['position'] = userMessage

    def getNextStep (self) :
        return Temperature()