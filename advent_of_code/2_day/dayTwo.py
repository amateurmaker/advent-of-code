
#! /usr/bin/env/ python3
print("Day two challenge")

# Open the file and read it
file = open('daytwo.txt', 'r')
Lines = file.readlines()

horizontal_dist = 0
depth = 0

for line in Lines:
    line = line.rstrip("\n")
    line_arr = line.split(' ')
    
    if (line_arr[0] == "down"):
        depth += int(line_arr[1])
    elif (line_arr[0] == "up"):
        depth -= int(line_arr[1])
    else:
        horizontal_dist += int(line_arr[1])

answer = horizontal_dist * depth
print(f"The part 1 answer is: {answer}")

horizontal_dist = 0
depth = 0
aim = 0
for line in Lines:
    line = line.rstrip("\n")
    line_arr = line.split(' ')
    
    if (line_arr[0] == "down"):
        aim += int(line_arr[1])
    elif (line_arr[0] == "up"):
        aim -= int(line_arr[1])
    else:
        horizontal_dist += int(line_arr[1])
        depth += (aim * int(line_arr[1]))

answer = horizontal_dist * depth
print(f"The part 2 answer is: {answer}")