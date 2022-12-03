
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
file = open('dayseven.txt', 'r')
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
    return data.split(",")

def convertStringToInt(data):
    new_list = []
    for element in data:
        new_list.append(int(element))
    return new_list

def getList(data):
    for line in data:
        return (line.split(','))

def getInt(data):
    new_lst = []
    for element in data:
        new_lst.append(int(element))
    return new_lst

def calculateFuelBasedOnMeadian(data):
    fuel = 0
    for element in data:
        fuel += abs(element - median)
    return fuel

def calculateFuelBasedOnMean(data):
    fuel = 0
    for element in data:
        for i in range(abs(element - mean)):
            fuel += i + 1
    return fuel

new_list = getInt(getList(Lines))
median = int(statistics.median(new_list))
# Whether to use floor or ceiling was a guess
mean = math.floor(statistics.mean(new_list))
print(f"The original mean is: {statistics.mean(new_list)} and the new mean is: {round(statistics.mean(new_list))}")
print(f"The answer for part 1 is: {calculateFuelBasedOnMeadian(new_list)}")
print(f"The answer for part 2 is: {calculateFuelBasedOnMean(new_list)}")

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# del Board[0:1]
# if (row.count('x') == 5):
