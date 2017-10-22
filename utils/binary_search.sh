#!/usr/bin/env bash

# Binary search of the lowest value for which a command returns a non-zero
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

