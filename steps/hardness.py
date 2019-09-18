from .position import Position

class Hardness():
    def __init__ (self) :
        self.dictionary = ['Какой жесткости матрас вам нужен']
        self.name = 'hardness'

    def getName (self) :
        return self.name
    
    def getText (self) :
        return self.dictionary[0]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['hardness'] = userMessage['original_utterance']

    def getNextStep (self) :        
        return Position()