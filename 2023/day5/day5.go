package main
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

var seeds []string
var seeds_counter [100]bool

// int mapping
const (
	start int = 0
	preseedtosoil = 1
	seedtosoil = 2
	presoiltofertiliser = 3
	soiltofertiliser = 4
	prefertilisertowater = 5
	fertilisertowater = 6
	prewatertolight = 7
	watertolight = 8
	prelighttotemperature = 9
	lighttotemperature = 10
	pretempteraturetohumidity = 11
	tempteraturetohumidity = 12
	prehumiditytolocation = 13
	humiditytolocation = 14
)

func resetCounter() {
	for i, _ := range seeds_counter {
		seeds_counter[i] = false;
	}
}

func convertToInt(data string) int {
	// string to int
	i, err := strconv.Atoi(data)
	if err != nil {
		// ... handle error
		panic(err)
	}

	return i
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func minFind(arr []string) int {
	min := convertToInt(arr[0])
	for _, num1 := range arr {
	   if convertToInt(num1) < min {
		  min = convertToInt(num1)
	   }
	}
	return min
 }
 

func main() {
	lines, err := readLines("p1.txt")
	var state int = start
	
	// Define a container to store the seeds
	
    check(err)
    for _, line := range lines {
        // Print each line for debugging
		// fmt.Println(line)

		res1 := strings.Split(line, " ")
		

		if state == 0 {
			for _, s := range res1 {
				if s == "seeds:" {
					// Move on to the next stage
					state = preseedtosoil
					seeds = res1[1:len(res1)]
					// fmt.Println(seeds)

					

					for i, _ := range seeds_counter {
						seeds_counter[i] = false;
					}

				}
			}
		}

		if state == preseedtosoil {
			if line == "seed-to-soil map:" {
				// fmt.Println("proceedig to seed to soil")
				state = seedtosoil
				resetCounter()
				continue
			}
		}

		if state == seedtosoil {
			if line == "" {
				// fmt.Println("done. next.\n")
				state = presoiltofertiliser
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}

			}
			// fmt.Println("seed to soil: ", seeds)
		}

		if state == presoiltofertiliser {
			if line == "soil-to-fertilizer map:" {
				// fmt.Println("proceedig to soil to fertiliser")
				state = soiltofertiliser
				resetCounter()
				continue
			}
		}

		if state == soiltofertiliser {
			if line == "" {
				// fmt.Println("donezo. next.\n")
				state = prefertilisertowater
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}
			}

			// fmt.Println("soil to fert: ", seeds)
		}

		if state == prefertilisertowater {
			if line == "fertilizer-to-water map:" {
				state = fertilisertowater
				resetCounter()
				continue
			}
		}

		if state == fertilisertowater {
			if line == "" {
				state = prewatertolight
				// fmt.Println("donezo. next.\n")
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}
			}

			// fmt.Println("fert to water: ", seeds)
		}

		if state == prewatertolight {
			if line == "water-to-light map:" {
				state = watertolight
				resetCounter()
				continue
			}
		}

		if state == watertolight {
			if line == "" {
				state = prelighttotemperature
				// fmt.Println("donezo. next.\n")
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}
			}

			// fmt.Println("water to light", seeds)
		}

		if state == prelighttotemperature {
			if line == "light-to-temperature map:" {
				state = lighttotemperature
				resetCounter()
				// fmt.Println("donezo. next.\n")
				continue
			}
		}

		if state == lighttotemperature {
			resetCounter()
			if line == "" {
				state = pretempteraturetohumidity
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
					
				}
			}
			// fmt.Println("light to temp", seeds)
		}


		if state == pretempteraturetohumidity {
			if line == "temperature-to-humidity map:" {
				state = tempteraturetohumidity
				resetCounter()
				// fmt.Println("donezo. next.\n")
				continue
			}
		}

		if state == tempteraturetohumidity {
			if line == "" {
				state = prehumiditytolocation
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}
				
			}
			// fmt.Println("temp to humid", seeds)
		}

		if state == prehumiditytolocation {
			if line == "humidity-to-location map:" {
				state = humiditytolocation
				resetCounter()
				// fmt.Println("donezo. next.\n")
				continue
			}
		}

		if state == humiditytolocation {
			if line == "" {
				// fmt.Println("DONE")
				continue
			}

			for idx, s := range seeds {

				h := convertToInt(res1[0])
				i := convertToInt(res1[1])
				j := convertToInt(res1[2])
				k := convertToInt(s)

				if k >= i && k <= i + j && !seeds_counter[idx]{
					var temp int = convertToInt(seeds[idx]) - (i - h)
					seeds[idx] = strconv.FormatInt(int64(temp), 10)
					seeds_counter[idx] = true
				}
			}

			// fmt.Println("humid to loc", seeds)
		}
    }


	fmt.Println("p1", minFind(seeds))
}
