from .hardness import Hardness
import random

class Intro:
    def __init__ (self) :
        self.dictionary = ['Hi, what\'s your bed size', 'Hello, what\'s your bed size']
        self.name = 'intro'

    def getName (self) :
        return self.name
    
    def getText (self) :
        index = random.randint(0,1)
        return self.dictionary[index]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['size'] = userMessage

    def getNextStep (self) :
        return Hardness()