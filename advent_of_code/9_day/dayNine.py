
#! /usr/bin/env/ python3
from calendar import c
import copy
from itertools import count
from lib2to3.pytree import convert
import sys
from collections import defaultdict
import statistics
import math
print("Day Nine challenge")

# Open the file and read it
file = open('daynine.txt', 'r')
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

new_list = []
for line in Lines:
    new_list.append(stripNewLine(convertString(line))) 

new_new_list = []
for element in new_list:
    sub_arr = []
    for number in element[0]:
        sub_arr.append(number)
    new_new_list.append(sub_arr)

print(new_new_list)

last_x = len(new_new_list) - 1
last_y = len(new_new_list[0]) - 1
# print(f"The last x is: {last_x} and the last y is: {last_y}")
count = 0
for i in range(len(new_new_list)):
    for j in range(len(new_new_list[i])):
        number = new_new_list[i][j]
        if (i == 0 and j == 0):
            if (number < new_new_list[i + 1][j] and number < new_new_list[i][j + 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("top left corner")
        elif (i == last_x and j == 0):
            if (number < new_new_list[i - 1][j] and number < new_new_list[i][j - 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("top right corner")
        elif (i == last_x and j == last_y):
            if (number < new_new_list[i - 1][j] and number < new_new_list[i][j - 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("bottom right")
        elif (i == 0 and j == last_y):
            if (number < new_new_list[i - 1][j] and number < new_new_list[i][j - 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("bottom left")
        elif (i == 0):
            if (number < new_new_list[i][j - 1] and number < new_new_list[i][j + 1] and number < new_new_list[i+1][j]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("top wall")
        elif (i == last_x):
            if (number < new_new_list[i][j - 1] and number < new_new_list[i][j + 1] and number < new_new_list[i-1][j]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("bottom wall")
        elif (j == last_y):
            if (number < new_new_list[i - 1][j] and number < new_new_list[i + 1][j] and number < new_new_list[i][j - 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("right wall")
        elif (j == 0):
            if (number < new_new_list[i - 1][j] and number < new_new_list[i + 1][j] and number < new_new_list[i][j + 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
        else:
            if (number < new_new_list[i - 1][j] and number < new_new_list[i + 1][j] and number < new_new_list[i][j - 1] and number < new_new_list[i][j + 1]):
                print(f"This number is the lowest: {number}")
                count += int(number) + 1
            # print("left wall")

print(f"the part 1 number is: {count}")

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# del Board[0:1]
# if (row.count('x') == 5):
