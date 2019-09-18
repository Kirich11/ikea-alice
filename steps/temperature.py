from .price import Price

class Temperature:
    def __init__ (self) :
        self.dictionary = ['Любите спать в тепле или прохладе?']
        self.name = 'temperature'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary[0]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['temperature'] = userMessage['original_utterance']

    def getNextStep (self) :        
        return Price()