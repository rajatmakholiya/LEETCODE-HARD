package main

import {
	"fmt"
	"math"
}

func firstMissingPositive ( nums []int) int {
	n := make(map[int]struct{})

	for _, num := range nums {
		set[num] = struct{}{}
	}
	sm := 1
	for {
		if(_, ok := set[sm]; !ok){
			return sm
		}
		sm ++
	}

}

