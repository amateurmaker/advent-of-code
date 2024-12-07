const fs = require('fs');

// Path to the text file
const filePath = 'input/day_four.txt';

const getTwoDVert = (twoDInput, len) => {
    const vertTwoDInput = [];
    for (let i = 0; i < len; i++) {
        const temp = [];
        for (let j = 0; j < twoDInput.length; j++) {
            temp.push(twoDInput[j][i]);
        }
        vertTwoDInput.push(temp);
    }
    return vertTwoDInput;
}

// Read the file (synchronously or asynchronously)
fs.readFile(filePath, 'utf8', (err, inputString) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    const twoDInput = inputString.split("\n");
    const word = 'XMAS';
    const splitString = word.split("");
    const reverseArray = splitString.reverse();
    const reverseWord = reverseArray.join("");
    const gridSize = twoDInput[0].length;  // The grid size is 10x10 based on the input
    let count = 0;
    const vertTwoDInput = getTwoDVert(twoDInput, gridSize);

    // Check horizontal occurrences
    for (let row = 0; row < twoDInput.length; row++) {
        count += twoDInput[row].split(word).length - 1;
        count += twoDInput[row].split(reverseWord).length - 1;
    }

    // Check vertical occurrences
    for (let row = 0; row < vertTwoDInput.length; row++) {
        const column = vertTwoDInput[row].join('');
        count += column.split(word).length - 1;
        count += column.split(reverseWord).length - 1;
    }

    // Check diagonal (top-left to bottom-right)
    for (let row = 0; row <= twoDInput.length - 4; row++) {
        for (let col = 0; col <= twoDInput[row].length - 4; col++) {
            // Check for the word "XMAS"
            if (twoDInput[row][col] === 'X' && twoDInput[row + 1][col + 1] === 'M' && twoDInput[row + 2][col + 2] === 'A' && twoDInput[row + 3][col + 3] === 'S') {
                count += 1;
            }
            // Check for the reversed word "SAMX"
            if (twoDInput[row][col] === 'S' && twoDInput[row + 1][col + 1] === 'A' && twoDInput[row + 2][col + 2] === 'M' && twoDInput[row + 3][col + 3] === 'X') {
                count += 1;
            }
        }
    }

    // Check diagonal (top-right to bottom-left)
    for (let row = 0; row <= twoDInput.length - 4; row++) {
        for (let col = twoDInput[row].length - 1; col >= 3; col--) {
            // Check for the word "XMAS"
            if (twoDInput[row][col] === 'X' && twoDInput[row + 1][col - 1] === 'M' && twoDInput[row + 2][col - 2] === 'A' && twoDInput[row + 3][col - 3] === 'S') {
                count += 1;
            }
            // Check for the reversed word "SAMX"
            if (twoDInput[row][col] === 'S' && twoDInput[row + 1][col - 1] === 'A' && twoDInput[row + 2][col - 2] === 'M' && twoDInput[row + 3][col - 3] === 'X') {
                count += 1;
            }
        }
    }

    console.log(`The result is: ${count}`);
});
