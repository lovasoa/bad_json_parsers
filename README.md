# Bad JSON parsers
[![Build Status](https://travis-ci.org/lovasoa/bad_json_parsers.svg?branch=master)](https://travis-ci.org/lovasoa/bad_json_parsers)

Exposing problems in json parsers of several programming languages.
The name of this repository is intentionally provocative.
Its goal is to document limitations of existing json parsers, not to denigrate the work of the many contributors who worked on the various libraries presented here.

## Introduction

Many JSON parsers (and many parsers in general) use [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
to parse nested structures.
This is very convenient while programming the parser, but it has consequenses on what the parser can parse:
indeed, the size of the [call stack](https://en.wikipedia.org/wiki/Call_stack) is usually limited to a value several orders of magnitude smaller
than the available RAM, and this implies that a program with too many levels of recursion will fail.

However, the [JSON specification](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf)
doesn't contain any limit on how deeply nested JSON structures can be.
This means that most JSON parsers fail on a valid input.

This repository contains tools to measure the limits of JSON parsers of different languages.

## How to use

This repository contains a script called [test_parser.sh](test_parser.sh) that takes a JSON parser and uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest JSON structure it fails to parse and print its nesting level.

The json parser must be a program that reads JSON on its standard input, and exits with a status of 0 if it managed to parse it and any other status if an error occured.

## How it works

[test_parser.sh](test_parser.sh) constructs json structures composed uniquely of nested arrays, and gives them to the program it tests. For instance, for a depth of 3, it builds the following json : `[[[]]]`. This allows to create a structure of only *2n* bytes that has *n* nesting levels.
It uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest structure for which the programm fails.

## Results

On my machine (Ubuntu Linux 4.10.0-35-generic SMP x86_64 with 8Gb RAM, 8.4 MB maximum stack size),
I found the following results, sorted from worst to best:

language        | json library                                                | nesting level | file size     | notes                         |
----------------| ----------------------------------------------------------- | ------------- | ------------- | ----------------------------- |
ruby            | [json](https://rubygems.org/gems/json/versions/1.8.3)       | 101           | 202 bytes     |
rust            | [serde_json](https://docs.serde.rs/serde_json/)             | 128           | 256 bytes     |
php             | `json_decode`                                               | 512           | 1024 bytes    | maximum depth is configurable |
python3         | [json](https://docs.python.org/3/library/json.html)         | 994           | 2.0 KB        | without sys.setrecursionlimit
C               | [jansson](https://jansson.readthedocs.io/)                  | 2049          | 4.0 KB        | 
java - gson     | [Gson](https://github.com/google/gson)                      | 5670          | 11.3 KB       |
javascript      | `JSON.parse`                                                | 5713          | 11.4 KB       |
java - jackson  | [Jackson](https://github.com/FasterXML/jackson-core)        | 6373          | 13   KB       |
C++             | [nlohmann::json](https://github.com/nlohmann/json)          | 13787         | 27.6 KB       | segfault
ruby            | [Oj](https://github.com/ohler55/oj)                         | ∞             | ∞             |
Haskell         | [Aeson](https://hackage.haskell.org/package/aeson)          | ∞             | ∞             | available RAM is the only limit

## Remarks

I tried to test the most popular json library of each language. If you want to add a new language or a new library,
feel free to open a pull request.

All the parameters were left to their defaut values. In particular, the result
for PHP is particular: `json_decode` accepts a `depth` parameter to configure
the maximum depth of the object to be parsed.
