#"!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:53:08 2022

@author: blablalf
"""

import sys

# Morpion part

# Display the game grid
def displayGrid(aState):
    print("   | 1 | 2 | 3 |")
    for lineIndex in range(len(aState)):
        line = " " + str(lineIndex+1) + " |"
        for case in aState[lineIndex]:
            if(case=="empty"):
                line = line + "   |"
            if(case=="X"):
                line = line + " X |"
            if(case=="O"):
                line = line + " O |"
        print(line)
    print("")
        
def writeNewCaseHuman(aState):
    displayGrid(aState)
    column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") : ").split(",")
    while (aState[int(line)-1][int(column)-1] != "empty"):
        column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") : ").split(",")
    aState[int(line)-1][int(column)-1] = "O"
    displayGrid(aState)

def writeNewCaseHuman2(aState):
    displayGrid(aState)
    column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") : ").split(",")
    while (aState[int(line)-1][int(column)-1] != "empty"):
        column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") : ").split(",")
    aState[int(line)-1][int(column)-1] = "X"
    displayGrid(aState)

#return "empty"; "equality"; "O"; "X"
def checkEnd(aState):
    end=True
    for line in aState:
        aCase=line[0]
        for case in line:
            if (case=="empty" or case != aCase):
                end=False
        if (end):
            return aCase
        end=True
    for columnIndex in range(len(aState[0])):
        aCase=aState[0][columnIndex]
        for line in aState:
            if (line[columnIndex]=="empty" or line[columnIndex] != aCase):
                end=False
        if (end):
            return aCase
        end=True
    if (aState[0][0] == aState[1][1] and aState[0][0] == aState[2][2] or aState[0][2] == aState[1][1] and aState[0][2] == aState[2][0]):
        return aState[1][1]
    for line in aState:
        if "empty" in line:
            return "empty"
    return "equality"

# MinMax Part
def writeNewCaseComputer(aState):
    bestScore = -1000 #We initialize the bes_score at the lowest value
    bestShotColumn = 0
    bestShotLine = 0
    for lineIndex in range(3):
        for columnIndex in range(3):
            if (aState[lineIndex][columnIndex] == "empty"):
                aState[lineIndex][columnIndex] = "X" #test value
                score = minMax(aState, False, False)
                aState[lineIndex][columnIndex] = "empty"
                if (score > bestScore):
                    bestScore = score
                    bestShotColumn = columnIndex
                    bestShotLine = lineIndex
    aState[bestShotLine][bestShotColumn]="X"
    
def minMax(aState, isComputerPlay, displayed=True):

    if (checkEnd(aState) == "X"): #computer
        return 100
    if (checkEnd(aState) == "O"): #human
        return -100
    if (checkEnd(aState) == "equality"):
        return 0
    if (isComputerPlay):
        bestScore = -1000 #worst score for computer
        for lineIndex in range(3):
            for columnIndex in range(3):
                if (aState[lineIndex][columnIndex] == "empty"):
                    aState[lineIndex][columnIndex] = "X"
                    score = minMax(aState, False)
                    aState[lineIndex][columnIndex] = "empty"
                    if (score > bestScore):
                        bestScore = score                    
        return bestScore
    else:
        bestScore = 1000 #worst score for player
        for lineIndex in range(3):
            for columnIndex in range(3):
                if (aState[lineIndex][columnIndex] == "empty"):
                    aState[lineIndex][columnIndex] = "O"
                    score = minMax(aState, True)
                    aState[lineIndex][columnIndex] = "empty"
                    if (score < bestScore):
                        bestScore = score                    
        return bestScore

# just for some funny others test
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(1000000000)
#print(sys.getrecursionlimit())
state = [["empty"]*3 for line in range(3)]

while checkEnd(state) == "empty":
    writeNewCaseHuman(state)
    if checkEnd(state) == "empty":
        print("Computer action :")
        writeNewCaseComputer(state)
        checkEnd(state)

displayGrid(state)
if checkEnd(state) == "equality":
    print("End of the game : it's an equality, it always finish like that")
if checkEnd(state) == "X":
    print("End of the game : it's a victory for the computer")
if checkEnd(state) == "O":
    print("End of the game : it's a victory for you, it's so rare")