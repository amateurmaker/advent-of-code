#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <string>

std::vector<std::stack<std::string>> traversePreviousLines(const std::vector<std::string> &previous_lines)
{
    std::vector<std::stack<std::string>> answer;
    const char num = previous_lines[previous_lines.size() - 2][previous_lines[previous_lines.size() - 2].size() - 2];
    int number = static_cast<int>(num - '0');

    for (int j = 0; j < number; j++)
    {
        std::stack<std::string> dummy_stack;
        answer.push_back(dummy_stack);
    }

    std::cout << "the number of stacks is: " << number << std::endl;

    for (int i = previous_lines.size() - 3; i >= 0; i--)
    {
        int count = -1;
        for (int j = 0; j < previous_lines[i].size(); j++)
        {
            ++count;
            if (previous_lines[i][j] == '[')
            {
                answer[count].push(previous_lines[i][j +])
            }
        }
        std::cout << "the previous line is: " << previous_lines[i] << std::endl;
    }

    return answer;
}

int main(void)
{
    int sum = 0;
    int sum2 = 0;
    std::fstream input_file;
    input_file.open("input.txt", std::ios::in); // open a file to perform read operation using file object
    if (input_file.is_open())
    {
        std::vector<std::stack<std::string>> crates;
        std::vector<std::string> previous_lines;
        std::string file_input;
        int sum = 0;
        bool stack_input_updated = false;

        while (getline(input_file, file_input))
        {

            if (file_input.find("move") != std::string::npos && !stack_input_updated)
            {
                // traverse the previous lines
                crates = traversePreviousLines(previous_lines);

                std::cout << "the line is: " << file_input << std::endl;
                stack_input_updated = true;
            }
            else
            {
                previous_lines.push_back(file_input);
            }
        }

        input_file.close(); // close the file object.

        // Part 1 answer:
        std::cout << "part 1 answer is: " << sum << std::endl;

        // Part 2 answer:
        std::cout << "part 2 answer is: " << sum2 << std::endl;
    }
}
