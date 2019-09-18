from .suggest import Suggest

class Price:
    def __init__ (self) :
        self.dictionary = ['Укажите свой бюджет.']
        self.name = 'price'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary[0]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['price'] = userMessage['original_utterance']

    def getNextStep (self) :
        return Suggest()