
#! /usr/bin/env/ python3
import copy
from itertools import count
print("Day two challenge")

# Open the file and read it
file = open('daythree.txt', 'r')
Lines = file.readlines()

common_character = [0] * 12
total_num_of_characters = len(Lines)

for line in Lines:
    for i in range(len(line)):
        if (line[i] == '1'):
            common_character[i] += 1

# print(total_num_of_characters)

gam = ''
ep = ''
for i in range(len(common_character)):
    if (common_character[i] > total_num_of_characters / 2):
        gam += '1'
    else:
        gam += '0'

for letter in gam:
    if letter == '1':
        ep += '0'
    else:
        ep += '1'

gam = int(gam, 2)
ep = int(ep, 2)

print(f"the answer for part 1 is: {gam * ep}")

oxy = ''
carbon_scrubber = ''

oxy_Lines_prev = copy.deepcopy(Lines)
carbon_Lines_prev = copy.deepcopy(Lines)

oxy_Lines = []
carbon_lines = []

common_character = [0] * 12

for i in range(len(common_character)):
    common_character = [0] * 12
    for line in oxy_Lines_prev:
        for j in range(len(line)):
            if (line[j] == '1'):
                common_character[j] += 1
    print(f"The index at this point is: {i}")
    print(f"The number of characters for this index is: {common_character[i]}")
    
    character_oxy = ''
    if (int(common_character[i]) >= int(len(oxy_Lines_prev) - int(common_character[i]))):
        character_oxy = '1'
    else:
        character_oxy = '0'

    for line in oxy_Lines_prev:
        if line[i] == character_oxy:
            oxy_Lines.append(line)

    oxy_Lines_prev = copy.deepcopy(oxy_Lines)
    oxy_Lines.clear()

    if (len(oxy_Lines_prev) == 1):
        print(f"The final line is: {oxy_Lines_prev}")
        break

for i in range(len(common_character)):
    common_character = [0] * 12
    for line in carbon_Lines_prev:
        print(f"out of the lines left: {line}")
        for j in range(len(line)):
            if (line[j] == '1'):
                common_character[j] += 1
    print(f"The index at this point is: {i}")
    print(f"The number of characters for this index is: {common_character[i]}")
    
    character_oxy = ''
    if (int(common_character[i]) < int(len(carbon_Lines_prev) - int(common_character[i]))):
        character_oxy = '1'
    else:
        character_oxy = '0'

    print(f"the character selected is: {character_oxy}")

    for line in carbon_Lines_prev:
        print(f"THe line is: {line}")
        if line[i] == character_oxy:
            carbon_lines.append(line)

    carbon_Lines_prev = copy.deepcopy(carbon_lines)
    carbon_lines.clear()

    if (len(carbon_Lines_prev) == 1):
        print(f"The final line is: {carbon_Lines_prev}")
        break
oxy_Lines_prev = oxy_Lines_prev[0].rstrip("\n")
# oxy_Lines_prev = int(oxy_Lines_prev, 2)
carbon_Lines_prev = carbon_Lines_prev[0].rstrip("\n")
# carbon_Lines_prev = int(carbon_Lines_prev, 2)


print(int(oxy_Lines_prev, 2) * int(carbon_Lines_prev, 2))