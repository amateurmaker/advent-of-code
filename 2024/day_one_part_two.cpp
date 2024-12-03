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

    // Create an unordered_map to store the count of each element
    std::unordered_map<int, int> countMap;

    // Loop through the vector and count occurrences of each element
    for (int num : vector2) {
        countMap[num]++;
    }

    // Calculate the distance
    int distance = 0;
    for (int i = 0; i < vector1.size(); i++) 
    {
        int num = vector1[i];
        if (countMap.find(num) != countMap.end())
            distance += vector1[i] * countMap[num];
    }

    std::cout << "The distance is: " << distance << std::endl;

    return 0;
}
