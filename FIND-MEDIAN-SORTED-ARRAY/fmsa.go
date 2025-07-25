package main

import (
	"fmt"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	i, j := 0, 0
	arr := []int{}

	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			arr = append(arr, nums1[i])
			i++
		} else {
			arr = append(arr, nums2[j])
			j++
		}
	}

	for i < len(nums1) {
		arr = append(arr, nums1[i])
		i++
	}

	for j < len(nums2) {
		arr = append(arr, nums2[j])
		j++
	}

	n := len(arr)
	if n%2 == 0 {
		return float64(arr[n/2-1]+arr[n/2]) / 2.0
	}
	return float64(arr[n/2])
}

func main() {
	nums1 := []int{1, 3}
	nums2 := []int{2}
	fmt.Println(findMedianSortedArrays(nums1, nums2)) // Output: 2.0
}
