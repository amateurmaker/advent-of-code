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
    let enabled = true;  // Initially mul instructions are enabled

    while (index < data.length) {
        // Find the first instance of "mul("
        const mulIndex = data.indexOf('mul(', index);
        const doIndex = data.indexOf('do()', index);
        const dontIndex = data.indexOf("don't()", index);

        // Check for the next instruction to process
        const nextIndex = Math.min(
            mulIndex === -1 ? Infinity : mulIndex,
            doIndex === -1 ? Infinity : doIndex,
            dontIndex === -1 ? Infinity : dontIndex
        );

        // If no valid instruction exists, break the loop
        if (nextIndex === Infinity) break;

        // Move the index forward to the next instruction to process
        index = nextIndex;

        // If we encounter "do()", enable mul instructions
        if (doIndex === index) {
            enabled = true;
            index += 4; // Move past the "do()"
        } else if (dontIndex === index) {
            enabled = false;
            index += 7; // Move past the "don't()"
        } else if (mulIndex === index && enabled) {
            const closeIndex = data.indexOf(')', mulIndex);
            if (closeIndex === -1) break; // No closing parenthesis found
            
            // Extract the part between "mul(" and ")"
            const mulContent = data.slice(mulIndex + 4, closeIndex); // content inside "mul()"
            
            // Split by comma to get the two numbers
            const numbers = mulContent.split(',');
            
            if (numbers.length === 2 && !isNaN(numbers[0]) && !isNaN(numbers[1])) {
                const num1 = parseInt(numbers[0].trim(), 10);
                const num2 = parseInt(numbers[1].trim(), 10);
                results += num1 * num2;
            }
            
            // Move the index forward to continue the search
            index = mulIndex + 1;
        } else {
            // Just move forward if it's not a valid mul or do/don't instruction
            index++;
        }
    }

    console.log(`The result is: ${results}`);
});
