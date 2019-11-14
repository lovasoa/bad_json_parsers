#!/usr/bin/env bash
# Find the shortest json structure that makes a given program fail.
# The given program should read a json value on its standard input and exit with
# a non-zero status if it failed to read the json value

ROOT=$(dirname "$0")
json_parsing_command="$*"

function test_deep_json() {
  # Run the json parser on a nested json array of depth n
  n=$1
  "$ROOT"/utils/deep_json_array.sh "$n" | $json_parsing_command 2>/dev/null >/dev/null
}

export -f test_deep_json
export json_parsing_command
export ROOT

"$ROOT"/utils/binary_search.sh test_deep_json 1 5000000
