#!/usr/bin/env bash

read -r json

export ON_ERROR_STOP=on
psql -c "select '$json'::json;"

