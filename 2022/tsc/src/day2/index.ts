import { readFileSync } from 'fs';
import { join } from 'path';
import internal from 'stream';

const computePoints = (a: string, b: string): number => {
    switch (a)
    {
    case 'A':
        if (b == 'Y')
        {
            return 2 + 6;
        }
        else if (b == 'X')
        {
            return 1 + 3;
        }
        else
        {
            return 3;
        }
        break;
    case 'B':
        if (b == 'Y')
        {
            return 2 + 3;
        }
        else if (b == 'X')
        {
            return 1 + 0;
        }
        else
        {
            return 3 + 6;
        }
        break;
    case 'C':
        if (b == 'Y')
        {
            return 2 + 0;
        }
        else if (b == 'X')
        {
            return 1 + 6;
        }
        else
        {
            return 3 + 3;
        }
        break;
    default:
        // code block
        return -1;
    }
};

const computePart2 = (a: string, b: string): number => {
    // X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    let value = '';

    switch(b)
    {
        case 'X':
            if (a == 'A')
            {
                value = 'Z';
            }
            else if (a == 'B')
            {
                value = 'X';
            }
            else
            {
                value = 'Y';
            }
            break;
        case 'Y':
            // Ending in a draw means both the first and second value are the same
            if (a == 'A')
            {
                value = 'X';
            }
            else if (a == 'B')
            {
                value = 'Y';
            }
            else 
            {
                value = 'Z';
            }
            break;
        case 'Z':
            if (a == 'A')
            {
                value = 'Y';
            }
            else if (a == 'B')
            {
                value = 'Z';
            }
            else
            {
                value = 'X';
            }
            break;
    }

    return computePoints(a, value);
};


const syncReadFile = (filename: string) => {
    const result: string = readFileSync(join(__dirname, filename), 'utf-8');
    const splitted: Array<string> = result.split("\n");

    // Initialise some variables   
    let sum: number = 1;
    let sum2: number = 1;

    splitted.map((file_input) => {
        const a: string = file_input[0];
        const b: string = file_input[2];

        sum += computePoints(a, b);
        sum2 += computePart2(a, b);;

    });

    console.log(`The answer for part 1 is: ${sum}`);
    console.log(`The answer for part 2 is: ${sum2}`);
}

export const day2 = () => {
    syncReadFile('./input.txt');
}