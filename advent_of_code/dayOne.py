#! /usr/bin/env/ python3
import copy

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


print("Day one part 2 of the challenge")

first_window = []
second_window = []
third_window = []

file = open('dayone.txt', 'r')
Lines = file.readlines()

first_window.append(int(Lines[0]))
first_window.append(int(Lines[1]))
first_window.append(int(Lines[2]))

second_window.append(int(Lines[1]))
second_window.append(int(Lines[2]))
second_window.append(int(Lines[3]))

third_window.append(int(Lines[2]))
third_window.append(int(Lines[3]))

if (sum(second_window) > sum(first_window) > 0):
    count =1
else:
    count = 0

for i in range(4, len(Lines)):
    line = int(Lines[i])

    second_window.append(line)
    third_window.append(line)

    if ((sum(second_window)) - (sum(first_window)) > 0):
       count += 1

    first_window = copy.deepcopy(second_window)
    second_window = copy.deepcopy(third_window)

    temp_var = third_window[1]
    third_window.clear()
    third_window.append(temp_var)

print("The answer is {}".format(count))
