from .suggest import Suggest

class Price:
    def __init__ (self) :
        self.dictionary = 'price'
        self.name = 'price'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['intro'] = userMessage

    def getNextStep (self) :
        return Suggest()