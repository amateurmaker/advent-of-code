const fs = require('fs').promises;

const number_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

const readLinesAsync = async (filePath) => {

    // This is adding the entire file content into the stack which is mad
    const fileContent = await fs.readFile(filePath, 'utf-8');
    const lines = fileContent.split('\n');

    let running_sum = 0;

    // var map = {};
    // // add a item
    // map[key1] = value1;
    // // or remove it
    // delete map[key1];
    // // or determine whether a key exists
    // key1 in map;

    count = 0
    lines.forEach((line) => {
        count += 1
        const store = []

        number_letters.map((word, idx) => {
            const index = line.indexOf(word);

            if (index !== -1) {
                line = line.replaceAll(word, word + (idx + 1) + word);
            }
        })

        for (let i = 0; i < line.length; i++) {
            if(Number(line[i])) {
                store.push(Number(line[i]));
            }    
        };

        running_sum += store[0] * 10
        running_sum += store[store.length - 1]

    });

    return running_sum;
};

const printResult = async () => {
    let result = await readLinesAsync("sample.txt");
    console.log(result)

    result = await readLinesAsync("inputa.txt");
    console.log(result)
};

// Call the asynchronous function
printResult();
