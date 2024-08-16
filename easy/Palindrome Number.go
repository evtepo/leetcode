package main

import (
	f "fmt"
)

func isPalindrome(x int) bool {
	val := f.Sprint(x)
	var left, right int = 0, len(val) - 1
	for left < right {
		if val[left] != val[right] {
			return false
		}

		left++
		right--

	}

	return true
}


func main() {
	f.Println(isPalindrome(-121))
}