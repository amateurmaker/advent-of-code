import * as readline from 'readline';
import { day1 } from './day1'
import { day2 } from './day2'
import { day3 } from './day3'
import { day4 } from './day4'

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const ask = () => {
    rl.question('Enter the day to run: [1/2/../q] ', (answer) => {
        switch (answer.toLowerCase()) {
            case '1':
                console.log('Generating day1 answer ====');
                day1();
                break;
            case '2':
                console.log('Generating day2 answer ====');
                day2();
                break;
            case '3':
                console.log('Generating day3 answer ====');
                day3();
                break;
            case '4':
                console.log('Generating day4 answer ====');
                day4();
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
