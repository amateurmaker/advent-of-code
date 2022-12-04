#include <iostream>
#include <fstream>
#include <unordered_map>

int getPriority(const char &c)
{
    return std::islower(c) ? (c - 'a' + 1) : (c - 'A' + 1 + 26);
}

// Can be used to debug an unordered_map in C++
template<typename K, typename V>
void print_map(std::unordered_map<K, V> const &m)
{
    for (auto const &pair: m) {
        std::cout << "{" << pair.first << ": " << pair.second << "}\n";
    }
}

char checkBadge(const std::string &first, const std::string &second, const std::string &third)
{
    // Unsorted hash table should do the trick
    std::unordered_map<char, int> map;

    // This should keep track of any duplicates
    std::unordered_map<char, int> duplicates;

    // Count characters in first string
    for (int i = 0; i < first.length(); i++)
    {
        if (duplicates[first[i]]++ > 0)
        {
            continue;
        }

        map[first[i]]++;
    }
    duplicates.clear();

    // Count characters in second string
    for (int i = 0; i < second.length(); i++)
    {
        if (duplicates[second[i]]++ > 0)
        {
            continue;
        }

        map[second[i]]++;
    }
    duplicates.clear();

    // If character is found 3 times then return that character
    for (int i = 0; i < third.length(); i++)
        if (map[third[i]] == 2)
            return third[i];

    // return some random character although this conditions should never happen
    return '*';
}

char check(const std::string &first, const std::string &second)
{
    // Unsorted hash table should do the trick
    std::unordered_map<char, int> map;

    // Count characters in first string
    for (int i = 0; i < first.length(); i++)
        map[first[i]]++;

    // If character is a duplicate then return that character
    for (int i = 0; i < second.length(); i++)
        if (map[second[i]] > 0)
            return second[i];

    // return some random character although this conditions should never happen
    return '*';
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
        int count = 0;
        std::string first_in_group;
        std::string second_in_group;
        std::string third_in_group;
        while (getline(input_file, file_input))
        {
            count++;

            if (count == 1)
            {
                first_in_group = file_input;
            }
            else if (count == 2)
            {
                second_in_group = file_input;
            }
            else
            {
                count = 0;
                third_in_group = file_input;
                char obtain_repeated_character_in_group = checkBadge(first_in_group, second_in_group, third_in_group);
                sum2 += getPriority(obtain_repeated_character_in_group);
            }

            int half = file_input.size() / 2;
            std::string first = file_input.substr(0, half);
            std::string second = file_input.substr(half);

            char obtain_repeated_character = check(first, second);
            int priority = getPriority(obtain_repeated_character);
            sum += priority;
        }
        input_file.close(); // close the file object.

        // Part 1 answer:
        std::cout << "part 1 answer is: " << sum << std::endl;

        // Part 2 answer:
        std::cout << "part 2 answer is: " << sum2 << std::endl;
    }
}
