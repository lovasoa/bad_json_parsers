package main

import (
	"os"

	"github.com/json-iterator/go"
)

func main() {
	x := []interface{}{}
	d := jsoniter.NewDecoder(os.Stdin)
	if err := d.Decode(&x); err != nil {
		os.Exit(1)
	}
}
