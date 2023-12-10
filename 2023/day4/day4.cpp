#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>

void stringToArray(std::string input, std::vector<int> &output)
{
    // initializing variables
    int start = 0;
    int end = 0;

    char dl = ' ';

    // run the loop until the end variable doesn't reach
    // the end of the string i.e, start = -1
    // string::npos is a constant static member that is
    // defined with -1 str.find_first_not_of(dl, end)) will
    // return the index of first character that is not
    // equal to dl
    while ((start = input.find_first_not_of(dl, end)) != std::string::npos)
    {
        // str.find(dl, start) will return the index of dl
        // from start index
        end = input.find(dl, start);

        // substr function return the substring of the
        // original string from the given starting index
        // to the given end index
        output.push_back(stoi(input.substr(start, end - start)));
    }
}

int main()
{
    std::string file = "p1.txt";
    std::ifstream fs(file);
    std::string line;
    int p1 = 0;

    // Number of additions there are
    std::vector<int> multiplier(100000, 0);
    int count = 0;

    while (std::getline(fs, line))
    {
        ++count;
        int points = -1;

        std::string delimiter = "|";
        int index = line.find(delimiter);

        delimiter = ":";
        int index_of_colon = line.find(delimiter);

        std::string winning = line.substr(index_of_colon + 2, index - index_of_colon - 3);
        std::string current = line.substr(index + 2); // token is "scott"

        std::vector<int> current_vect;
        std::vector<int> winning_vect;
        stringToArray(current, current_vect);
        stringToArray(winning, winning_vect);

        for (int i = 0; i < winning_vect.size(); i++)
        {
            std::vector<int>::iterator it = std::find(current_vect.begin(), current_vect.end(), winning_vect[i]);

            if (it != current_vect.end())
                ++points;
        }

        if (points >= 0)
        {
            // Part 1 stuff
            p1 += std::pow(2, points);

            // Part 2 stuff: Get the current multiplier and apply it
            int current_multiplier = multiplier[count - 1] + 1;
            for (int j = 0; j < points + 1; j++)
            {
                multiplier[count + j] += 1 * current_multiplier;
            }
        }
    }

    int p2 = 0;
    for (int i = 0; i < count; i++)
    {
        p2 += multiplier[i] + 1;
    }
    
    std::cout << "part 1: " << p1 << std::endl;
    std::cout << "part 2: " << p2 << std::endl;
}