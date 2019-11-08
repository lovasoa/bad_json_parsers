package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
)

func main() {
	x := []interface{}{}
	bytes, _ := ioutil.ReadAll(os.Stdin)
	err := json.Unmarshal(bytes, &x)
	if err != nil {
		os.Exit(1)
	}
}
