package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput(instr string) ([]int, int) {
	var tnkrs = []int{}
	x := strings.ReplaceAll(instr, "(", "")
	y := strings.ReplaceAll(x, ")", "")
	z := strings.ReplaceAll(y, " ", "")
	vals := strings.Split(z, ",")
	tbbls := vals[len(vals)-1]
	ttnkrs := vals[:len(vals)-1]
	for i := range ttnkrs {
		num := ttnkrs[i]
		tmpi, _ := strconv.Atoi(num)
		tnkrs = append(tnkrs, tmpi)
	}
	bbls, _ := strconv.Atoi(tbbls)
	return tnkrs, bbls
}

func fillage(tnkr int, bbls int) (int, int) {
	filled, rem := bbls/tnkr, bbls%tnkr
	return filled, rem
}

func initCountMap(tnkrs []int) map[int]int {
	x := make(map[int]int)
	for _, tnkr := range tnkrs {
		x[tnkr] = 0
	}
	return x
}

func check4match(tnkrs []int, bbls int) bool {
	for _, siz := range tnkrs {
		if siz == bbls {
			return true
		}
	}
	return false
}

// pass list of tankers starting with first tanker see how many fit
//  return list of tanker sizes and counts and a remainder (if any)
func findFit(primary []int, rest []int, bbls int, tnkrs []int) {
	x := initCountMap(tnkrs)
	for _, tnkr := range primary {
		//tnkr := primary[i]
		filled, rem := fillage(tnkr, bbls)
		if rem == 0 {
			x[tnkr] = filled
			fmt.Println("found option", x)
		}
		if rem != 0 {
			x[tnkr] = filled
			if check4match(rest, rem) {
				x[rem] = 1
				fmt.Println("found option", x)
			} else {
			}
		}
	}
}

func optomize(bbls int, tnkrs []int) {
	doTimes := len(tnkrs) - 1
	x := tnkrs[:]
	for t := 0; t <= doTimes; t++ {
		car := x[:1]
		cdr := x[1:]
		findFit(car, cdr, bbls, tnkrs)
		x = append(cdr, car...)

	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		tnkrs, bbls := parseInput(scanner.Text())
		optomize(bbls, tnkrs)
	}
}
