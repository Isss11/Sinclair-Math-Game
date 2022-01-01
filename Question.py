#This class is stil a work in progress -- trying to clean up the program and make it more object-oriented.
class Question:
    def __init__(self, gameInstance, questionType): #this is initializing the question, and assigning some original values to allocate memory
        self.gameInstance = gameInstance
        self.firstNumber = self.gameInstance.generateNumber()
        self.secondNumber = self.gameInstance.generateNumber()
        self.questionType = questionType
        self.answerTrue = False

        if (self.questionType == 0):
            self.correctAnswer = self.firstNumber + self.secondNumber
        elif (self.questionType == 1):
            self.correctAnswer = self.firstNumber - self.secondNumber
        elif (self.questionType == 2):
            self.correctAnswer = self.firstNumber * self.secondNumber
        else:
            while (self.secondNumber == 0):
                self.secondNumber = self.gameInstance.generateNumber()

            self.correctAnswer = self.firstNumber // self.secondNumber
            #this is integer division -- might split up division into two types

    def getFirstNumber(self):
        return self.firstNumber

    def getSecondNumber(self):
        return self.secondNumber

    def getCorrectAnswer(self):
        return self.correctAnswer 

    def getUserAnswer(self):
        return self.userAnswer

    def getAnswerTrue(self):
        return self.answerTrue

    def acceptUserAnswer(self):
        if (self.questionType == 0):
            self.userAnswer = int(input("What is {0} + {1}?\n".format(self.firstNumber, self.secondNumber)))
        elif (self.questionType == 1):
            self.userAnswer = int(input("What is {0} - {1}?\n".format(self.firstNumber, self.secondNumber)))
        elif (self.questionType == 2):
            self.userAnswer = int(input("What is {0} x {1}?\n".format(self.firstNumber, self.secondNumber)))
        else:
            self.userAnswer = int(input("What is {0} / {1}?\n".format(self.firstNumber, self.secondNumber)))

        return self.userAnswer

    def checkAnswer(self):
        self.answerTrue = bool(self.correctAnswer == self.userAnswer)

        return self.answerTrue