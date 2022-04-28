#!/usr/bin/env python3
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
        
def writeNewCaseHuman(aState):
    column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") :").split(",")
    while (aState[int(line)-1][int(column)-1] != "empty"):
        column, line = input("Saisissez en chiffre votre colonne et votre ligne séparé par une virgule (exemple : pour la colonne 2 et la ligne 1 on écrira \"2,1\") :").split(",")
    aState[int(line)-1][int(column)-1] = "O"
    displayGrid(aState)
    print(checkEnd(aState))

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
    if (aState[0][0] == aState[1][1] and aState[0][0] == aState[2][2] or aState[0][2] == aState[1][1] and aState[0][2] == aState[2][0]):
        return aState[1][1]
    for line in aState:
        if "empty" in line:
            return "empty"
    return "equality"

# MinMax Part
def writeNewCaseComputer(aState):
    bestScore = -1000
    bestShotColumn = 0
    bestShotLine = 0
    for lineIndex, line in enumerate(aState):
        for columnIndex, case in enumerate(line):
            if (case == "empty"):
                case = "X"
                #test value
                count = 0
                score = minMax(aState, False)
                case = "empty"
                if (score > bestScore):
                    bestScore = score
                    bestShotColumn = columnIndex
                    bestShotLine = lineIndex
    aState[lineIndex][columnIndex]="X"
    
def minMax(aState, isHumanPlay):
    if (checkEnd(aState) == "X"):
        return 100
    if (checkEnd(aState) == "O"):
        return -100
    if (checkEnd(aState) == "equality"):
        return 0
    if (isHumanPlay):
        bestScore = -1000
        bestShotColumn = 0
        bestShotLine = 0
        for line in aState:
            for case in line:
                if (case == "empty"):
                    case = "X"
                    score = minMax(aState, False)
                    case = "empty"
                    if (score > bestScore):
                        bestScore = score                    
        return bestScore
    else:
        bestScore = 1000
        bestShotColumn = 0
        bestShotLine = 0
        for line in aState:
            for case in line:
                if (case == "empty"):
                    case = "X"
                    score = minMax(aState, True)
                    case = "empty"
                    if (score < bestScore):
                        bestScore = score                    
        return bestScore

print(sys.getrecursionlimit())
sys.setrecursionlimit(570000)
print(sys.getrecursionlimit())
state = [["empty"]*3 for line in range(3)]

displayGrid(state)

while checkEnd(state) == "empty":
    writeNewCaseHuman(state)
    writeNewCaseComputer(state)
    
print(checkEnd(state))