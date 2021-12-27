#! /usr/bin/env/ python3

print("Day one challenge")

# Open the file and read it
file = open('dayone.txt', 'r')
Lines = file.readlines()
 
count = 0
prevNum = int(Lines[0])
for i in range(1, len(Lines)):
    # Convert line from str to int
    line = int(Lines[i])
    
    # Check if there is an increase
    if (line - prevNum > 0):
        count += 1

    # Update the previous number 
    prevNum = line

print("The answer is {}".format(count))
