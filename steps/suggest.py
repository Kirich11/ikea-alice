class Suggest:
    def __init__ (self) :
        self.dictionary = 'suggest'
        self.name = 'suggest'
        self.trans = {
            'size' : 'размер',
            'position' : 'поза сна', 
            'temperature' : 'температура сна',
            'price' : 'бюджет',
            'hardness': 'жесткость'
        }

    def getName (self) :
        return self.name

    def getText (self) :
        return self.dictionary

    def saveAnswer(self, userSession, userMessage):
        return

    def getResult (self, userSession) :
        result = "Ваши предпочтения:\r\n"
        d = userSession['answers']
        for k in d:
            result +=  self.trans[k] + "––" + str(d[k]) + "\r\n"
        return result
    
    def getNextStep(self):
        return Suggest()