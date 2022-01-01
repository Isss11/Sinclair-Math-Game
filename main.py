#-------------------------------------------------------------------------------
# Name:        sinclairMath.py
# Purpose:
#
# Author:      isss1
#
# Created:     17-12-2021
# Copyright:   (c) isss1 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Game import *
from Question import *
from HighScore import *

"""
Here is the general outline for the 'engine of the game'.

Side Note: Could probably just store the type of game, chosen file, score and hearts in a class (import from another file).

- Indication of the start of the game
- Pick between multiplication, division, adding, and subtraction.
- Choose what kind of list you want to get tested on, this will be from file inputs. I will create easier ones that work well with the program,
but the user can play around with the program and give harder ones (e.g. for long division).
- Then the user is assigned 3 hearts, and gets given random questions. This while loop structure will continue until all of those hearts are gone.
- XP points are awarded for each correct answer; hearts are taken away for each wrong one.
- Once the game is finished, the user can input there name should there be a highscore -- this will be stored in a file and be output on the screen.
"""
def main():
    print("Hello! Welcome to Sinclair Math!")

    #creation of game -- create class, and loop
    gameInstance = gameInstanceCreator()
    
    while (gameInstance.getRemainingHearts() > 0):
        answerCorrect = False
        givenQuestion = Question(gameInstance, gameInstance.getGameType())
        userAnswer = givenQuestion.acceptUserAnswer()
        answerCorrect = givenQuestion.checkAnswer()
        gameInstance.gameRoundUpdate(givenQuestion, 10, -1)
    
    #once the game is finished, check the list for the top 10 highscores -- user can input there name (needs 2 files or lists)

    gameHighScore = HighScore("highScoreNumbers.txt", "highScoreNames.txt")
    gameHighScore.compareScore(gameInstance.getPoints())
    

#The following code was from a previous attempt at programming this program (for reference)

def gameInstanceCreator(): #this is just lumping in the initial creation of the gameInstance
    gameType = int(input("Do play the addition (0), subtraction (1), multiplication (2), or division (3) game? Input the corresponding number.\n"))
    numberListName = input("Enter the file name of the numbers list you want to practice.\n")

    numberSet = []

    numberOfElements = assignNumbersList(numberSet, numberListName)

    gameInstance = Game(gameType, numberSet, 3, numberOfElements)

    return gameInstance

def assignNumbersList(numberSet, listName):
    numberOfElements = 0

    infile = open(listName, "r")

    for line in infile:
        numberSet.append(int(line))
        numberOfElements += 1

    infile.close()

    return numberOfElements

main()