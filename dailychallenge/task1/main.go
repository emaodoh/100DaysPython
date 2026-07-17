package main

import (
	"fmt"
)

func main(){
	for x := 1; x <=5; x++{
		for y := 1; y <= x; y++{
			fmt.Print(y)
		}
        fmt.Println()
	}
}