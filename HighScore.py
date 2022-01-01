class HighScore:
    def __init__(self, fileNameNumbers, fileNameNames):
        self.fileNameNumbers = fileNameNumbers
        self.fileNameNames = fileNameNames
        self.HighScoreNumbers = []
        self.HighScoreNames = []
        self.totalScores = 10 #this is just to demonstrate the at the total amount of scoreos in the highscores will be 10

        infileNumbers = open(self.fileNameNumbers, "r") #don't need to use 'self' as I desire to keep this as a local variable

        for i in range (self.totalScores): #going through file with high score numbers and storing them in an array
            self.HighScoreNumbers.append(int(infileNumbers.readline()))

        #now going to run through the file with the corresponding (to the high score numbers) high score names and store them in an array

        infileNames = open(self.fileNameNames, "r")

        for i in range (self.totalScores):
            self.HighScoreNames.append((infileNames.readline()).rstrip())

    def compareScore(self, score):
        self.score = score

        for i in range (self.totalScores):
            if (self.score > self.HighScoreNumbers[i]):
                self.insertScore(score, i)
                self.insertName(i)
                break


    def insertScore(self, score, index):
        for i in range (self.totalScores - 2, index - 1, -1): #starting at the second last index and decrementing, stops at any number smaller then the index
            self.HighScoreNumbers[i + 1] = self.HighScoreNumbers[i]

        self.HighScoreNumbers[index] = self.score #inserting in the score

        outfile = open(self.fileNameNumbers, "w")

        for i in range (self.totalScores):
            if (i == self.totalScores - 1): #don't want to print a newline with the final value in the list
                print(self.HighScoreNumbers[i], file=outfile, end = "")
            else:
                print(self.HighScoreNumbers[i], file=outfile)
    
    def insertName(self, index):
        for i in range (self.totalScores - 2, index - 1, -1):
            self.HighScoreNames[i + 1] = self.HighScoreNames[i]

        self.HighScoreNames[index] = (input("You made it on the leaderboard! Enter your name here: ")).rstrip()

        outfile = open(self.fileNameNames, "w")

        for i in range (self.totalScores):
            if (i == self.totalScores - 1): #don't want to print a newline with the final value in the list
                print(self.HighScoreNames[i], file=outfile, end = "")
            else:
                print(self.HighScoreNames[i], file=outfile)