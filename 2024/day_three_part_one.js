const fs = require('fs');

// Path to the text file
const filePath = 'input/day_three.txt';

// Read the file (synchronously or asynchronously)
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    let results = 0;
    let index = 0;

    while (index < data.length) {
        // Find the first instance of "mul("
        const mulIndex = data.indexOf('mul(', index);
        if (mulIndex === -1) break; // No more "mul(" found
        
        // Find the first instance of the closing parenthesis after "mul("
        const closeIndex = data.indexOf(')', mulIndex);
        if (closeIndex === -1) break; // No closing parenthesis found
        
        // Extract the part between "mul(" and ")"
        const mulContent = data.slice(mulIndex + 4, closeIndex); // content inside "mul()"
        
        // Split by comma to get the two numbers
        const numbers = mulContent.split(',');
        
        if (numbers.length === 2 && !isNaN(numbers[0]) && !isNaN(numbers[1])) {
            const num1 = parseInt(numbers[0].trim(), 10);
            const num2 = parseInt(numbers[1].trim(), 10);
            results += num1 * num2
        }
        
        // Move the index forward to continue the search
        index = mulIndex + 1;
    }

    console.log(`The result is: ${results}`)
});