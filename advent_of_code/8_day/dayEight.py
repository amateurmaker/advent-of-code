
#! /usr/bin/env/ python3
from calendar import c
import copy
from itertools import count
from lib2to3.pytree import convert
import sys
from collections import defaultdict
import statistics
import math
print("Day five challenge")

# Open the file and read it
file = open('dayeight.txt', 'r')
Lines = file.readlines()

# Obtain the board information
def convertStringtoList(string):
    return list(string.split(" "))

def returnMoves(data):
    return list(data.split(","))

def removeEmptyStringsFromList(data):
    return [string for string in data if string != ""]


# val = input("Do you want the answer for part 1 or 2? ")
# val = int(val)
# if (val == 1 or val == 2):
#     pass
# else:
#     print("invalid input, defaulting to part 1")
#     val = 1

# if (val == 1):
#     use_part_one = True
# else:
#     use_part_one = False

def convertString(data):
    return data.split(" ")

def stripNewLine(data):
    for index in range(len(data)):
        data[index] = data[index].rstrip("\n")
    return data

def getList(data):
    for line in data:
        return (line.split(','))

def getInt(data):
    new_lst = []
    for element in data:
        new_lst.append(int(element))
    return new_lst

def countDis(str):
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)

new_list = []
for line in Lines:
    new_list.append(stripNewLine(convertString(line))) 

count = 0
for element in new_list:
    for i in range(4):
        if (countDis(element[-i - 1]) == 2):
            count += 1
        elif (countDis(element[-i - 1]) == 4):
            count += 1
        elif (countDis(element[-i - 1]) == 3):
            count += 1
        elif (countDis(element[-i - 1]) == 7):
            count += 1
print(count)

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# del Board[0:1]
# if (row.count('x') == 5):
