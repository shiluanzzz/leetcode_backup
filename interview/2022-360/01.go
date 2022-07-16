package main

import (
	"fmt"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var s string
	var ans = 0
	_, _ = fmt.Scanf("%s", &s)
	for i := 1; i <= len(s); i++ {
		for j := 0; j <= len(s)-i; j++ {
			if len(s)-i-j/i < ans {
				break
			}
			ss := s[j : i+j]
			fmt.Println(ss)
			ans = max(strings.Count(s, ss), ans)
		}
	}
	fmt.Printf("%d", ans)
}
