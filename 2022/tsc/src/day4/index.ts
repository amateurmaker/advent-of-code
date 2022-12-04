import { readFileSync } from 'fs';
import { join } from 'path';

const taskIsContainedWithin = (one: Array<number>, two: Array<number>): number => {
    if (one[0] >= two[0] && one[0] <= two[1])
    {
        if (one[1] >= two[0] && one[1] <= two[1])
        {
            return 1;
        }
    }

    return 0;
}

const taskPartialOverlap = (one: Array<number>, two: Array<number>): number => {
    if (one[1] >= two[0] && one[1] <= two[1])
    {
            return 1;
    }

    return 0;
}

const checkOverlappingTasks = (task_one: Array<number>, task_two: Array<number>): number => {
    if (taskIsContainedWithin(task_one, task_two))
    {
        return 1;
    }

    if (taskIsContainedWithin(task_two, task_one))
    {
        return 1;
    }

    return 0;
}

const checkPartialOverlappingTasks = (task_one: Array<number>, task_two: Array<number>): number => {
    if (taskPartialOverlap(task_one, task_two))
    {
        return 1;
    }

    if (taskPartialOverlap(task_two, task_one))
    {
        return 1;
    }

    return 0;
}

const syncReadFile = (filename: string) => {
    const result: string = readFileSync(join(__dirname, filename), 'utf-8');
    const splitted: Array<string> = result.split("\n");

    // Initialise some variables   
    let sum: number = 0;
    let sum2: number = 0;

    splitted.map((file_input) => {
        let pair_one:string = file_input.slice(0, file_input.indexOf(","));
        let pair_two:string = file_input.slice(file_input.indexOf(",") + 1);

        let pair_one_first:string = pair_one.slice(0, pair_one.indexOf("-"));
        let pair_one_second:string = pair_one.slice(pair_one.indexOf("-") + 1);

        let pair_two_first:string = pair_two.slice(0, pair_two.indexOf("-"));
        let pair_two_second:string = pair_two.slice(pair_two.indexOf("-") + 1);

        const task_one: Array<number> = [parseInt(pair_one_first), parseInt(pair_one_second)];
        const task_two: Array<number> = [parseInt(pair_two_first), parseInt(pair_two_second)];

        sum += checkOverlappingTasks(task_one, task_two);
        sum2 += checkPartialOverlappingTasks(task_one, task_two);
    });

    console.log(`The answer for part 1 is: ${sum}`);
    console.log(`The answer for part 2 is: ${sum2}`);
}

export const day4 = () => {
    syncReadFile('./input.txt');
}