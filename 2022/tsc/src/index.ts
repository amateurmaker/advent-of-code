import * as readline from 'readline';
import { day1 } from './day1/day1'

let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const ask = () => {
    rl.question('Enter the day to run: [1/2/../q] ', (answer) => {
        switch (answer.toLowerCase()) {
            case '1':
                day1();
                console.log('Generating day1 answer ====');
                break;
            case '2':
                console.log('Generating day2 answer ====');
                break;
            case '3':
                console.log('Generating day3 answer ====');
                break;
            case 'q':
                console.log("Goodbye");
                rl.close();
                process.exit();
            default:
                console.log('Invalid answer!');
        }
        ask();
    });
}

ask();
