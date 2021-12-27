#! /usr/bin/env/ python3

print("Day one challenge")

# Open the file and read it
file = open('dayone.txt', 'r')
Lines = file.readlines()
 
isFirstLine = True
count = 0
prevNum = 0
for line in Lines:
    # Convert line from str to int
    line = int(line)
    if (isFirstLine):
        isFirstLine = False
    elif (line - prevNum > 0):
        count += 1
    
    prevNum = line

print("The answer is {}".format(count))