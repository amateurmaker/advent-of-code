#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
 #include <numeric>


int main(void)
{
      std::fstream input_file;
      input_file.open("input.txt", std::ios::in); // open a file to perform read operation using file object
      if (input_file.is_open())
      {
            std::string file_input;
            std::vector<int> food;
            int sum;
            while (getline(input_file, file_input))
            {
                  std::cout << file_input << " " << std::endl; // print the data of the string

                  if (file_input.empty())
                  {
                        food.push_back(sum);
                        sum = 0;
                  }
                  else
                  {
                        sum += std::stoi(file_input);
                  }
            }

            // Don't forget the last sum
            food.push_back(sum);

            input_file.close(); // close the file object.
            std::sort(food.begin(), food.end());

            // Part 1 answer:
            std::cout << "the max amount of food is: " << food.back() << std::endl;

            // Part 2 answer:
            int sum_of_elems = std::accumulate(food.end() - 3 , food.end(), 0);
            std::cout << "the max amount of food the last 3 elves are carrying is: " << sum_of_elems << std::endl;
      }
}
