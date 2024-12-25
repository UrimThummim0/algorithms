package main

import "fmt"

// pythagoreanTripletsBruteForce finds the Pythagorean triplet where the sum of its
// numbers is 1000, using a brute force approach.
func pythagoreanTripletsBruteForce() {
	// Iterate through all possible values of a, b, and c, and check if they form
	// a Pythagorean triplet whose sum is 1000.
	for a := 1; a <= 1000; a++ {
		for b := a + 1; b < 1000-a; b++ {
			for c := b + 1; c < 1000-b; c++ {
				if a*a+b*b == c*c && a+b+c == 1000 {
					fmt.Println("a =", a, "b =", b, "c =", c)
					return
				}
			}
		}
	}
}

func main() {
	fmt.Println("Pythagorean Triplets")
	pythagoreanTripletsBruteForce()
}
