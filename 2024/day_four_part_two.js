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
    let count = 0;

    // Check diagonal (top-left to bottom-right)
    for (let row = 1; row <= twoDInput.length - 2; row++) {
        for (let col = 1; col <= twoDInput[row].length - 2; col++) {
            // Check for the word "XMAS"
            if (twoDInput[row][col] !== 'A') continue;
            if ((twoDInput[row - 1][col - 1] === 'M' && twoDInput[row + 1][col + 1] === 'S') && (twoDInput[row - 1][col + 1] === 'M' && twoDInput[row + 1][col - 1] === 'S')) {
                count += 1
                continue
            }

            if ((twoDInput[row - 1][col - 1] === 'S' && twoDInput[row + 1][col + 1] === 'M') && (twoDInput[row - 1][col + 1] === 'M' && twoDInput[row + 1][col - 1] === 'S')) {
                count += 1
                continue
            }

            if ((twoDInput[row - 1][col - 1] === 'M' && twoDInput[row + 1][col + 1] === 'S') && (twoDInput[row - 1][col + 1] === 'S' && twoDInput[row + 1][col - 1] === 'M')) {
                count += 1
                continue
            }

            if ((twoDInput[row - 1][col - 1] === 'S' && twoDInput[row + 1][col + 1] === 'M') && (twoDInput[row - 1][col + 1] === 'S' && twoDInput[row + 1][col - 1] === 'M')) {
                count += 1
                continue
            }
        }
    }

    console.log(`The result is: ${count}`);
});
