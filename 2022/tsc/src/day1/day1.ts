import { readFileSync } from 'fs';
import { join } from 'path';

// ✅ read file SYNCHRONOUSLY
const accumulate = ({ food }: { food?: Array<number> }): number => {
    let third_food: number = (food || []).length - 3
    let second_food: number = (food || []).length - 2
    let first_food: number = (food || []).length - 1

    // Returns NaN if food is empty
    const sum: number = (food || [])[third_food] + (food || [])[second_food] + (food || [])[first_food]
    return sum;
};

const syncReadFile = (filename: string) => {
    const result: string = readFileSync(join(__dirname, filename), 'utf-8');
    const splitted: Array<string> = result.split("\n");

    // Initialise some variables   
    let sum = 0;
    let food: Array<number> = [];

    splitted.map((value) => {
        console.log(value); // 👉️ "hello world hello world ..."

        if (value === '') {
            console.log("The string is empty")
            food.push(sum);
            sum = 0;
        }
        else {
            sum += parseInt(value);
        }
    });

    const food_sorted: number[] = food.sort((n1,n2) => n1 - n2);
    console.log(`The answer for part 1 is: ${food_sorted[food_sorted.length - 1]}`);
    console.log(`The answer for part 2 is: ${accumulate({food: food_sorted})}`);
}

export const day1 = () => {
    syncReadFile('./input.txt');
}