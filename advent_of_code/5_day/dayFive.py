
#! /usr/bin/env/ python3
import copy
from itertools import count
import sys
print("Day five challenge")

# Open the file and read it
file = open('dayfive.txt', 'r')
Lines = file.readlines()

# Obtain the board information
def convertStringtoList(string):
    return list(string.split(" "))

def returnMoves(data):
    return list(data.split(","))

def removeEmptyStringsFromList(data):
    return [string for string in data if string != ""]

def printVerticalorHorizontalLines(data):
    max_x = 0
    max_y = 0

    lines = []
    
    for element in data:
        element_arr = element.split("->")
        x_y_0 = element_arr[0].split(",")
        x_y_1 = element_arr[1].split(",")

        x0 = int(x_y_0[0])
        y0 = int(x_y_0[1])

        start = [x0, y0]
        
        x1 = int(x_y_1[0])
        y1 = int(x_y_1[1])
        end = [x1, y1]

        line_points = [start, end]

        
        
        if (x0 > max_x):
            max_x = x0
        
        if (x1 > max_x): 
            max_x = x1

        if (y0 > max_y):
            max_y = y0
        
        if (y1 > max_y): 
            max_y = y1

        lines.append(line_points)

    return max_x, max_y, lines

max_x, max_y, lines = (printVerticalorHorizontalLines(Lines))

# Form the sea bed
arr = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

def findSmallest(uno, dos):
    if (uno < dos):
        return uno, dos
    else:
        return dos, uno

val = input("Do you want the answer for part 1 or 2? ")
val = int(val)
if (val == 1 or val == 2):
    pass
else:
    print("invalid input, defaulting to part 1")
    val = 1

if (val == 1):
    use_part_one = True
else:
    use_part_one = False

# Iterate through the liens
for line in lines:
    # The x is flat
    if (line[0][0] == line[1][0]):
        # print(f"THe vertical flat line is: {line}")
        first, second = findSmallest(line[0][1], line[1][1])
        for i in range(first, second + 1):
            arr[i][line[0][0]] += 1
    
    elif (line[0][1] == line[1][1]):
        # print(f"THe horizontal flat line is: {line}")
        first, second = findSmallest(line[0][0], line[1][0])
        for i in range(first, second + 1):
            arr[line[0][1]][i] += 1
    elif (use_part_one == False):
        # print(f"The line is slanted: {line}")
        gradient = (line[0][1] - line[1][1])/(line[0][0] - line[1][0])
        intercept = line[0][1] - gradient * line[0][0]
        first, second = findSmallest(line[0][0], line[1][0])
        for i in range(first, second + 1):
            y = int((gradient * i) + intercept)
            arr[y][i] += 1
            # print(f"The x is: {i} and the y is: {y}")

count = 0
for row in arr:
    for element in row:
        if (element >= 2):
            count +=1

print(f"The answer for part 1 is: {count}") if use_part_one else print(f"The answer for part 2 is: {count}")

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# del Board[0:1]
# if (row.count('x') == 5):
