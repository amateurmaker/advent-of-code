#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>  // For stringstream
#include <string>   // For string
#include <bits/stdc++.h> // For sorting

int main() {
    std::ifstream inputFile("input/day_one.txt");
    
    if (!inputFile) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;  // Exit if the file could not be opened
    }

    std::vector<int> vector1, vector2;  // Two vectors to store the values

    // Read line by line and push the values into a vector
    int val1, val2;
    while (inputFile >> val1 >> val2) {
        vector1.push_back(val1);  // Store the first value in vector1
        vector2.push_back(val2);  // Store the second value in vector2
    }

    // Sort the vectors
    std::sort(vector1.begin(), vector1.end());
    std::sort(vector2.begin(), vector2.end());

    // Calculate the distance
    int distance = 0;
    for (int i = 0; i < vector2.size(); i++) distance += std::abs(vector1[i] - vector2[i]);

    std::cout << "The distance is: " << distance << std::endl;

    return 0;
}
