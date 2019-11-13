#!/usr/bin/env bash

json=$(</dev/stdin)

export ON_ERROR_STOP=on
psql -c "select '$json'::json;"

