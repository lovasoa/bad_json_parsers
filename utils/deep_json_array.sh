#!/usr/bin/env bash 

function repeat_string {
  # Repeat a string n times
  # Usage: ./repeat_string.sh string number_of_repetitions
  string="$1"
  number_of_repetitions=$2
  printf "$string%.s" $(seq $number_of_repetitions)
}

depth=$1
repeat_string '[' $depth
repeat_string ']' $depth
