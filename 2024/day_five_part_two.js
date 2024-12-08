const fs = require('fs');

fs.readFile('input/day_five.txt', 'utf8', (err, advent) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    if (advent.endsWith("\n")) advent = advent.slice(0, -1);
    let [rules, instructions] = advent.split("\n\n").map(x => x.split("\n"));

    rules = rules.map(e => e.split('|')).map(e => e.map(Number));
    instructions = instructions.map(e => e.split(',')).map(e => e.map(Number));

    const lines = [];

    const logic = (rule, numbers) => {
        const [index1, index2] = [numbers.indexOf(rule[0]), numbers.indexOf(rule[1])];
        return (index1 !== -1 && index2 !== -1 && index1 > index2) ? [false, index1, index2] : [true, index1, index2];
    };

    // Part One
    for (const numbers of instructions) {
        if (rules.every(rule => logic(rule, numbers)[0])) lines.push(numbers);
    }
    console.log(`Part one: ${lines.reduce((s, e) => s + e[Math.floor(e.length / 2)], 0)}`);

    // Get all the lines that were not in part 1
    const unordered_instructions = instructions.filter(e => !lines.includes(e));
    let note = true
    while (note) {
        let returnType = false;

        // For each of the instructions, check if they match  the rules
        for (const n of unordered_instructions)
            rules.some(rule => {
                const [index1, index2] = [n.indexOf(rule[0]), n.indexOf(rule[1])];
                let pass = (index1 !== -1 && index2 !== -1 && index1 > index2) ? false : true
                if (!pass) {
                    // Since it did not pass, swap the numbers in the instructions
                    [n[index1], n[index2]] = [n[index2], n[index1]];

                    // Since we swapped one of the numbers we have to go through this whole rodeo again
                    returnType = true;
                }
            });
        
        note = returnType;
    }

    // This will add all the centre numbers
    console.log(`Part two: ${unordered_instructions.reduce((s, e) => s + e[Math.floor(e.length / 2)], 0)}`);
});

