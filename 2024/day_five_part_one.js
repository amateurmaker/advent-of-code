const fs = require('fs');

// Path to the text file

// Read the file (synchronously or asynchronously)
fs.readFile(
    'input/day_five.txt',
    'utf8',
    (err, inputString) => {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }

        let answer = 0;

        const rules = []
        const instructions = []
        const inputs = inputString.split("\n");
        for (let i = 0; i < inputs.length; i++) {
            if (inputs[i].indexOf('|') > -1) {
                rules.push(inputs[i])
                continue
            }

            if (inputs[i] === "") continue
            
            instructions.push(inputs[i].split(","))
        }

        for (let i = 0; i < instructions.length; i++) {
            let pass = true;
            for (let j = 0; j < rules.length && pass; j++) {
                const [a, b] = rules[j].split("|")
                const first = instructions[i].indexOf(a)
                const second = instructions[i].indexOf(b)

                if (first === -1) continue
                if (second === -1) continue
                if ( first > second) pass = false
            }

            if (pass) {
                console.log(`The instructions are: ${i + 1}`)
                const middle = instructions[i].length / 2
                const idx = middle.toFixed(0) - 1
                answer += parseInt(instructions[i][idx])
            }
        }

        console.log(`The result is: ${answer}`);
});
