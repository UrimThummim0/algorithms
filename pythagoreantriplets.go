package main

import "fmt"

// pythagoreanTripletsBruteForce finds the Pythagorean triplet where the sum of its
// numbers is 1000, using a brute force approach.
func pythagoreanTripletsBruteForce(sum int) {
	// Iterate through all possible values of a, b, and c, and check if they form
	// a Pythagorean triplet whose sum is 1000.
	for a := 1; a <= sum; a++ {
		for b := a + 1; b < sum-a; b++ {
			for c := b + 1; c < sum-b; c++ {
				if a*a+b*b == c*c && a+b+c == sum {
					fmt.Println("a =", a, "b =", b, "c =", c)
					return
				}
			}
		}
	}
}

func main() {
	fmt.Println("Pythagorean Triplets")
	pythagoreanTripletsBruteForce(10000)
}
