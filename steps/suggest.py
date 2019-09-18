class Suggest:
    def __init__ (self) :
        self.dictionary = 'suggest'
        self.name = 'suggest'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        return

    def getResult (self, userSession) :
        result = ""
        d = userSession['answers']
        for k in d:
            result +=  k + " " + d[k] + "\r\n"
        return result
    
    def getNextStep(self):
        return Suggest()