#!/usr/bin/env bash

read -r json
depth=$((${#json} / 2))

export ON_ERROR_STOP=on
sql="select (repeat('[', $depth) || repeat(']', $depth))::json;"
echo "Making the following query: $sql"
psql -c "$sql"
