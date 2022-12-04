
#! /usr/bin/env/ python3
import copy
from itertools import count
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
                for row_index in row:
                    if (row_index == data):
                        row_index = 'x'
                
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

def partTwoAnswer(brd, data):
    for board in brd:
        if board:
            count = 0
            for row in board:
                for element in row:
                    if (element != 'x'):
                        count += int(element)
            partOne = count
            partTwo = int(data)
            print(f"The answer for part 2 is: {partOne * partTwo}")
            sys.exit(0)


def checkIfLastBoard(brd, data):
    count = 0
    for board in brd:
        if board:
            count += 1
    
    if count == 1:
        partTwoAnswer(brd, data)
        sys.exit(0)

def evaluateRows(data, Board, some_bool):
    for index in range(len(Board)):
        skip_board = False
        for row in Board[index]:
            if (skip_board):
                continue

            try:
                for row_index in range(len(row)):
                    if (row[row_index] == data):
                        row[row_index] = 'x'
                        if (row.count('x') == 5):
                            checkIfLastBoard(Board, data)
                            Board[index] = []
                            skip_board = True
                            break

                    count = 0
                    for local_row in Board[index]:
                        if (local_row[row_index] == 'x'):
                            count += 1

                        if (count == 5):
                            checkIfLastBoard(Board, data)
                            Board[index] = []
                            skip_board = True
                            break

            except ValueError as e:
                print("ERROR!")
                continue
            
        

# Play Each Move
bingo_numbers = returnMoves(moves)
last_num = bingo_numbers[len(bingo_numbers) - 1]
last_num_bool = False

val = input("Enter either 1 or 2: ")
if (val != '1' or val != '2'):
    print("invalid input, defaulting to part 1")
    val = "1"
    
if (val == "1"):
    for num in bingo_numbers:
        # This is for Part 1
        checkRows(num, Board)
else:
    for num in bingo_numbers:
        if (num == last_num):
            print(f"this is the last number: {num}")
            last_num_bool = True
            break
        else:
            evaluateRows(num, Board, True)

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")