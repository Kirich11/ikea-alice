class Suggest:
    def __init__ (self) :
        self.dictionary = 'suggest'
        self.name = 'suggest'

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        userSession['answers']['intro'] = userMessage

    def getResult (self, userSession) :
        result = ""
        d = userSession['answers']
        for k in d:
            result +=  d + " " + d[k] + "\r\n"
        return result