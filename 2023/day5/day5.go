package main
import (
	"fmt"
	"os"
	"bufio"
)

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

func main() {
	lines, err := readLines("sample.txt")
    check(err)
    for _, line := range lines {
        fmt.Println(line)
    }
}
