import random

class Game:
    def __init__(self, gameType, numbersList, remainingHearts, numberOfElements):
        self.gameType = gameType
        self.numbersList = numbersList
        self.remainingHearts = remainingHearts
        self.points = 0
        self.numberOfElements = numberOfElements

    def addPoints(self, addingPoints):
        self.points += addingPoints

        return self.points

    def changeHeart(self, change):
        self.remainingHearts += change

        return self.remainingHearts

    def getPoints(self):
        return self.points

    def getRemainingHearts(self):
        return self.remainingHearts

    def getGameType(self):
        return self.gameType

    def getNumbersList(self):
        return self.numbersList

    def generateNumber(self):
        return self.numbersList[random.randint(0, self.numberOfElements - 1)]

    def gameRoundUpdate(self, question, pointChange, heartChange):
        if (question.getAnswerTrue() == True):
            self.addPoints(pointChange)
            print("Correct answer! You have {0} point(s) and {1} heart(s) remaining.".format(self.getPoints(), self.getRemainingHearts()))
        else:
            self.changeHeart(heartChange)
            print("Sorry, your answer is wrong. The correct answer is {0}. You have {1} point(s) and {2} heart(s) remaining.".format(question.getCorrectAnswer(), self.getPoints(), self.getRemainingHearts()))