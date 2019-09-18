from .temperature import Temperature

class Position:
    def __init__ (self) :
        self.dictionary = 'position'
        self.name = 'position'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['position'] = userMessage

    def getNextStep (self) :
        return Temperature()