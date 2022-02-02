
#! /usr/bin/env/ python3
import copy
from itertools import count
from lib2to3.pytree import convert
import sys
from collections import defaultdict
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

def multiplyFish():
    global fishMap
    # Instead of making a flat list create a dictionary to clump similar fish states together
    updatedFishMap = defaultdict(int)  
    
    # Go to each fish to change its state, take note that [fish-1] could possibly add a new key which is not allowed
    # while iterating over fish map, hence use defaultdict as a temporary storage to add keys first
    # then transfer the value back to fishMap                                            
    for fish, count in fishMap.items():
        if fish == 0:                           # Take all fishes that need to reproduce
            updatedFishMap[6] += count          # Reset their reproduction date by changing their state
            updatedFishMap[8] += count          # Add all the fishes offspring to the highest state
        else:
            updatedFishMap[fish-1] += count     # Move all fish to the state below theirs

        fishMap = updatedFishMap                # Update the main list


for line in Lines:
    line_arr = convertString(line)
    line_arr = convertStringToInt(line_arr)

fishMap = defaultdict(int) 
for fish in line_arr:                            
    if fish not in fishMap:                  
        fishMap[fish] = 0                    
    fishMap[fish] += 1   

for i in range(256):
    multiplyFish()

print(f"The answer for part 1 is: {sum(fishMap.values())}")

# Extra code that could be useful
# oxy_Lines_prev = copy.deepcopy(Lines)
# carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# del Board[0:1]
# if (row.count('x') == 5):
