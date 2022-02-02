
#! /usr/bin/env/ python3
import copy
from itertools import count
from pickle import FALSE
from re import A
import sys
print("Day four challenge")

# Open the file and read it
file = open('dayfour.txt', 'r')
Lines = file.readlines()

# Obtain the moves
moves = Lines[0]

# Obtain the board information
Bingo = []
Board = []
def convertStringtoList(string):
    return list(string.split(" "))

def returnMoves(data):
    return list(data.split(","))

def removeEmptyStringsFromList(data):
    return [string for string in data if string != ""]

for index in range(1, len(Lines)):
    if (Lines[index] == '\n'):
        Board.append(copy.deepcopy(Bingo))
        Bingo.clear()
    else:
        rows_as_strings_in_list = convertStringtoList(Lines[index].rstrip("\n"))
        final_rows_as_strings_in_list = removeEmptyStringsFromList(rows_as_strings_in_list)
        Bingo.append(final_rows_as_strings_in_list)

Board.append(copy.deepcopy(Bingo))
del Board[0:1]

def printBoard(data):
    for bingo in data:
        print(bingo)

def countTheBoard(brd, num):
    print(f"Counting the following: {brd}")
    count = 0
    for row in brd:
        for element in row:
            if (element != 'x'):
                count += int(element)
    partOne = count - int(num)
    partTwo = int(num)
    print(f"The answer for part 1 is: {partOne * partTwo}")
    sys.exit(0)

def clearBoard():
    return []


def checkRows(data, Board):
    for board in Board:
        for row in board:
            try:
                for lala in row:
                    if (lala == data):
                        lala = 'x'
                
                number = row.index(data)

                if (row.count('x') == 4):
                    print(f"THIS IS IT: {Board}")
                    countTheBoard(board, data)
                    # Count up the rest of the elements and print the answer

                count = 0
                for local_row in board:
                    if (local_row[number] == 'x'):
                        count += 1

                    if (count == 4):
                        countTheBoard(board, data) 
            except ValueError as e:
                continue
            
            row[number] = 'x'
        

# Play Each Move
bingo_numbers = returnMoves(moves)
last_num = bingo_numbers[len(bingo_numbers) - 1]
for num in bingo_numbers:
    checkRows(num, Board)

# printBoard(Board)

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")