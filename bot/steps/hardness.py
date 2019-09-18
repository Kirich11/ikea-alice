from .position import Position

class Hardness():
    def __init__ (self) :
        self.dictionary = ['hardness']
        self.name = 'hardness'

    def getName (self) :
        return self.name
    
    def getText (self) :
        return self.dictionary[0]

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['intro'] = userMessage

    def getNextStep (self) :        
        return Position()