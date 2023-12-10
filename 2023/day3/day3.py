import sys
import copy

from helper import Number, check, convert_to_2d_arr, Check, check_if_same

class Coords:
    x = -1
    y = -1

def checkdict(input):
    for thing in thisdict.keys():
        if check_if_same(input, thing):
            print(f"{input.x} {input.y}")
            return True
        
    return False

# Read the file
file = open('p1.txt').read().strip()
# file = open('sample.txt').read().strip()
lines = file.split('\n')

# The following is the list comprehension way of doing it
# G = [[c for c in line] for line in lines]
G = convert_to_2d_arr(lines)

lrow = len(G)       # Number of rows
lcolumn = len(G[0]) # Number of columns

list_of_numbers = []


is_number = False
for i in range(lrow):
    new_number = Number()
    for j in range(lcolumn):
        character: str = G[i][j]
        
        if (character.isnumeric()):
            if (not is_number):
                is_number = True
                
                new_number.start = [i, j]
                new_number.number += character

            else:
                new_number.number += character

        else:
            if (is_number):
                is_number = False
                new_number.end = [i, j - 1]

                list_of_numbers = list_of_numbers[:]
                list_of_numbers.append(copy.deepcopy(new_number))

                new_number.number = ''
    
    if (is_number):
        is_number = False
        new_number.end = [i, j - 1]

        list_of_numbers = list_of_numbers[:]
        list_of_numbers.append(copy.deepcopy(new_number))

        new_number.number = ''


is_number_cleared = False
lrow = len(G) - 1
p1 = 0
checker = Check(lcolumn, lrow, G)
for num in list_of_numbers:
    # print(f"{num.number} with {num.start[0]}, {num.start[1]} to {num.end[0]}, {num.end[1]}")
    is_number_cleared = False

    # print(num.number)

    for j in range(num.start[1], num.end[1] + 1):
        
        if (is_number_cleared):
            continue

        i = num.start[0]

        is_number_cleared = checker.check_top_left(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue

        is_number_cleared = checker.check_left(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_bottom_left(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_bottom(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_bottom_right(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_right(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_top_right(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue
        
        is_number_cleared = checker.check_top(i, j)
        if is_number_cleared:
            # print(f"{num.number}")
            p1 += int(num.number)
            continue

# print(p1)

is_number_cleared = False
lrow = len(G) - 1
p2 = 0
thisdict = {}

for num in list_of_numbers:

    is_number_cleared = False

    for j in range(num.start[1], num.end[1] + 1):
        
        if (is_number_cleared):
            continue

        i = num.start[0]
        is_number_cleared = checker.check_top_left(i, j, True)

        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i - 1) + '00000' + str(j - 1)
            print(f"8The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]

            continue

        is_number_cleared = checker.check_left(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            
            print(f"7The number is cleared: {num.number} with index: {index}")
            index = str(i - 1) + '00000' + str(j)
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_bottom_left(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i - 1) + '00000' + str(j + 1)
            print(f"6The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_bottom(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i) + '00000' + str(j + 1)
            print(f"5The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_bottom_right(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i + 1) + '00000' + str(j + 1)
            print(f"4The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_right(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i + 1) + '00000' + str(j)
            print(f"3The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_top_right(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i + 1) + '00000' + str(j - 1)
            print(f"2The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue
        
        is_number_cleared = checker.check_top(i, j, True)
        if is_number_cleared:
            # Add the key to the dictionary 
            index = str(i) + '00000' + str(j - 1)
            print(f"1The number is cleared: {num.number} with index: {index}")
            if index in thisdict.keys():
                temp = thisdict[index]
                temp.append(num.number)
                thisdict[index] = temp
            else:
                thisdict[index] = [num.number]
                
            continue

for thing in thisdict.keys():
    if len(thisdict[thing]) == 2:
        print(thisdict[thing])
        p2 += int(thisdict[thing][0]) * int(thisdict[thing][1])

print(p2)