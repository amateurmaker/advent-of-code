import { readFileSync } from 'fs';
import { join } from 'path';


const check = (first: string, second: string): string => {
    let map: any = {

    };

    // Count characters in first string
    for (let i = 0; i < first.length; i++)
        map[first[i]] = 1;

    // If character is a duplicate then return that character
    for (let i = 0; i < second.length; i++)
        if (map[second[i]] > 0)
            return second[i];

    // return some random character although this conditions should never happen
    return '*';
}

const getPriority = (c: string): number => {
    return (c == c.toLowerCase()) ? (c.charCodeAt(0) - 'a'.charCodeAt(0) + 1) : (c.charCodeAt(0) - 'A'.charCodeAt(0) + 1 + 26);
}

const checkBadge = (first: string, second: string, third: string): string => {
    // Unsorted hash table should do the trick
    let map:any  = {

    };

    let duplicates:any  = {

    };

    // Count characters in first string
    for (let i: number = 0; i < first.length; i++) {
        map[first[i]] = 1;
    }

    // Count characters in second string
    for (let i: number = 0; i < second.length; i++) {
        if (duplicates[second[i]] === 1) {
            continue
        }

        if (map[second[i]] === 1) {
            duplicates[second[i]] = 1;
            map[second[i]] = 2;
        } else {
            duplicates[second[i]] = 1;
            map[second[i]] = 1;
        }
        
    }

    // If character is found 3 times then return that character
    for (let i: number = 0; i < third.length; i++)
        if (map[third[i]] == 2)
            return third[i];

    // return some random character although this conditions should never happen
    return '*';
};


const syncReadFile = (filename: string) => {
    const result: string = readFileSync(join(__dirname, filename), 'utf-8');
    const splitted: Array<string> = result.split("\n");

    // Initialise some variables   
    let count: number = 0;
    let sum: number = 0;
    let sum2: number = 0;

    let first_in_group: string = "";
    let second_in_group: string = "";
    let third_in_group: string = "";

    splitted.map((file_input) => {
        count++;

        if (count == 1) {
            first_in_group = file_input;
        }
        else if (count == 2) {
            second_in_group = file_input;
        }
        else {
            count = 0;
            third_in_group = file_input;
            const obtain_repeated_character_in_group: string = checkBadge(first_in_group, second_in_group, third_in_group);
            sum2 += getPriority(obtain_repeated_character_in_group);
        }

        const half: number = file_input.length / 2;
        let first: string = file_input.slice(0, half);
        let second: string = file_input.slice(half);

        const repeated_character: string = check(first, second);
        const priority: number = getPriority(repeated_character);
        sum += priority;

    });

    console.log(`The answer for part 1 is: ${sum}`);
    console.log(`The answer for part 2 is: ${sum2}`);
}

export const day3 = () => {
    syncReadFile('./input.txt');
}