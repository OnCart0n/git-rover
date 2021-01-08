package main

import (
	"fmt"
	"net"
	"os"
)

// GetIP Get ip from Domain
func GetIP(domain string) []string {
	ipaddrs, err := net.LookupHost(domain)
	if err != nil {
		return nil
	}
	return ipaddrs
}

func main() {
	if len(os.Args) > 1 {
		res := GetIP(os.Args[1])
		for _, ip := range res {
			fmt.Printf("%s\n", ip)
		}
	}
}
