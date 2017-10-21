#!/usr/bin/env bash

parser="$1"

function repeat_string {
  # Repeat a string n times
  printf "$1%.s" $(seq $2)
}

function deep_json_array {
  repeat_string '[' $1
  repeat_string ']' $1
}

function dichotomic_search {
  # Dichotomic search of the lowest value for which a command returns a non-zero
  # exit code
  test_prog="$1"
  min=$2
  max=$3
  while [ $((min+1)) -lt $max ]
  do
    middle=$(((min+max)/2))
    $test_prog $middle
    if [ $? = 0 ]
    then
      min=$middle
    else
      max=$middle
    fi
  done
  echo $max
}

function test_deep_json {
  # Run the json parser on a nested json array of depth n
  n=$1
  deep_json_array $n | $parser 2>/dev/null >/dev/null
}

dichotomic_search test_deep_json 1 100000
