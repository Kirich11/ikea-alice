from .suggest import Suggest

class Price:
    def __init__ (self) :
        self.dictionary = ['Можете указать свой бюджет?']
        self.name = 'price'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['price'] = userMessage

    def getNextStep (self) :
        return Suggest()