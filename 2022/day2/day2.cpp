#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

int computePoints(const char a, const char b)
{
    switch (a)
    {
    case 'A':
        if (b == 'Y')
        {
            return 2 + 6;
        }
        else if (b == 'X')
        {
            return 1 + 3;
        }
        else
        {
            return 3;
        }
        break;
    case 'B':
        if (b == 'Y')
        {
            return 2 + 3;
        }
        else if (b == 'X')
        {
            return 1 + 0;
        }
        else
        {
            return 3 + 6;
        }
        break;
    case 'C':
        if (b == 'Y')
        {
            return 2 + 0;
        }
        else if (b == 'X')
        {
            return 1 + 6;
        }
        else
        {
            return 3 + 3;
        }
        break;
    default:
        // code block
        return -1;
    }
}

int computePart2(const char& a, const char& b)
{
    // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    char value;
    char second_value;

    switch(b)
    {
        case 'X':
            if (a == 'A')
            {
                value = 'Z';
            }
            else if (a == 'B')
            {
                value = 'X';
            }
            else
            {
                value = 'Y';
            }
            break;
        case 'Y':
            // Ending in a draw means both the first and second value are the same
            if (a == 'A')
            {
                value = 'X';
            }
            else if (a == 'B')
            {
                value = 'Y';
            }
            else 
            {
                value = 'Z';
            }
            break;
        case 'Z':
            if (a == 'A')
            {
                value = 'Y';
            }
            else if (a == 'B')
            {
                value = 'Z';
            }
            else
            {
                value = 'X';
            }
            break;
    }

    return computePoints(a, value);
}

int main(void)
{
    std::fstream input_file;
    input_file.open("input.txt", std::ios::in); // open a file to perform read operation using file object
    if (input_file.is_open())
    {
        std::string file_input;
        int sum = 0;
        int sum2 = 0;
        while (getline(input_file, file_input))
        {
            char a = file_input[0];
            char b = file_input[2];

            sum += computePoints(a, b);
            sum2 += computePart2(a, b);;
        }
        input_file.close(); // close the file object.

        // Part 1 answer:
        std::cout << "part 1 answer is: " << sum << std::endl;

        // Part 2 answer:
        std::cout << "part 2 answer is: " << sum2 << std::endl;
    }
}
