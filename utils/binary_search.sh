#!/usr/bin/env bash

# Binary search of the lowest value for which a command returns a non-zero
# exit code
test_prog="$1"
min=$2
max=$3

$test_prog $min
if [ $? != 0 ]; then
  echo "Cannot apply a binary search. Input program failed even with an input of $min" 1>&2
  exit 1
fi

$test_prog $max
if [ $? = 0 ]; then
  echo "∞"
  exit 0
fi

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

