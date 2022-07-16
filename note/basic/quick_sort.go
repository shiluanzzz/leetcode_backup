package main

import "fmt"

func partition(arr_p *[]int, low, high int) int {
	arr := *arr_p
	max_value := arr[high]
	low_index := low - 1
	for i := low; i < high; i++ {
		if arr[i] < max_value {
			low_index += 1
			arr[low_index], arr[i] = arr[i], arr[low_index]
		}
	}
	low_index += 1
	arr[low_index], arr[high] = arr[high], arr[low_index]
	return low_index
}
func quick_sort(arr *[]int, low, high int) {
	if low < high {
		mid := partition(arr, low, high)
		quick_sort(arr, low, mid-1)
		quick_sort(arr, mid+1, high)
	}
}
func main() {
	arr := []int{3, 2, 1, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(arr)
	quick_sort(&arr, 0, len(arr)-1)
	fmt.Println(arr)
}
