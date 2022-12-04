#include <iostream>
#include <fstream>
#include <unordered_map>
#include <numeric>
#include <algorithm>
#include <numeric>

int taskIsContainedWithin(const std::pair<int, int> &one, const std::pair<int, int> &two)
{
    if (one.first >= two.first && one.first <= two.second)
    {
        if (one.second >= two.first && one.second <= two.second)
        {
            return 1;
        }
    }

    return 0;
}

int taskPartialOverlap(const std::pair<int, int> &one, const std::pair<int, int> &two)
{
    if (one.second >= two.first && one.second <= two.second)
    {
            return 1;
    }

    return 0;
}

int checkOverlappingTasks(const std::pair<int, int> &task_one, const std::pair<int, int> &task_two)
{
    if (taskIsContainedWithin(task_one, task_two))
    {
        return 1;
    }

    if (taskIsContainedWithin(task_two, task_one))
    {
        return 1;
    }

    return 0;
}

int checkPartialOverlappingTasks(const std::pair<int, int> &task_one, const std::pair<int, int> &task_two)
{
    if (taskPartialOverlap(task_one, task_two))
    {
        return 1;
    }

    if (taskPartialOverlap(task_two, task_one))
    {
        return 1;
    }

    return 0;
}

int main(void)
{
    int sum = 0;
    int sum2 = 0;
    std::fstream input_file;
    input_file.open("input.txt", std::ios::in); // open a file to perform read operation using file object
    if (input_file.is_open())
    {
        std::string file_input;
        int sum = 0;
        while (getline(input_file, file_input))
        {
            std::string pair_one = file_input.substr(0, file_input.find(","));
            std::string pair_two = file_input.substr(file_input.find(",") + 1);

            std::string pair_one_first = pair_one.substr(0, pair_one.find("-"));
            std::string pair_one_second = pair_one.substr(pair_one.find("-") + 1);

            std::string pair_two_first = pair_two.substr(0, pair_two.find("-"));
            std::string pair_two_second = pair_two.substr(pair_two.find("-") + 1);

            std::pair<int, int> task_one = std::make_pair<int, int>(std::stoi(pair_one_first), std::stoi(pair_one_second));
            std::pair<int, int> task_two = std::make_pair<int, int>(std::stoi(pair_two_first), std::stoi(pair_two_second));
            sum += checkOverlappingTasks(task_one, task_two);
            sum2 += checkPartialOverlappingTasks(task_one, task_two);
        }

        input_file.close(); // close the file object.

        // Part 1 answer:
        std::cout << "part 1 answer is: " << sum << std::endl;

        // Part 2 answer:
        std::cout << "part 2 answer is: " << sum2 << std::endl;
    }
}
