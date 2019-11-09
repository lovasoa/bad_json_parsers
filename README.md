# Nesting levels for JSON parsers
[![Build Status](https://travis-ci.org/lovasoa/bad_json_parsers.svg?branch=master)](https://travis-ci.org/lovasoa/bad_json_parsers)

Documenting how JSON parsers of several programming languages deal with deeply nested structures.

## Introduction

Many JSON parsers (and many parsers in general) use [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
to parse nested structures.
This is very convenient while programming the parser, but it has consequences on what the parser can parse:
indeed, the size of the [call stack](https://en.wikipedia.org/wiki/Call_stack) is usually limited to a value several orders of magnitude smaller
than the available RAM, and this implies that a program with too many levels of recursion will fail.

The two most recent JSON standards [RFC 8259](https://tools.ietf.org/html/rfc8259) and [RFC 7159](https://tools.ietf.org/html/rfc7159) both say "An implementation may set limits on the maximum depth of nesting". 
However, the [ECMA-404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) specification
doesn't contain any limit on how deeply nested JSON structures can be. 

This means that there is not a defined level of nesting which is correct or incorrect with regard to the JSON specification, and JSON parsers may differ when parsing nested structures.

This repository contains tools to measure the nesting limits of JSON parsers of different languages.

## How to use

This repository contains a script called [test_parser.sh](test_parser.sh) that takes a JSON parser and uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest JSON structure it fails to parse and print its nesting level.

The json parser must be a program that reads JSON on its standard input, and exits with a status of 0 if it managed to parse it and any other status if an error occurred.

## How it works

[test_parser.sh](test_parser.sh) constructs json structures composed uniquely of nested arrays, and gives them to the program it tests. For instance, for a depth of 3, it builds the following json : `[[[]]]`. This allows to create a structure of only *2n* bytes that has *n* nesting levels.
It uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest structure for which the program fails.

## Results

On my machine (Ubuntu Linux 4.10.0-35-generic SMP x86_64 with 8Gb RAM, 8.4 MB maximum stack size),
I found the following results, sorted from least nesting to most nesting:

language        | json library                                                | nesting level | file size     | notes                         |
----------------| ----------------------------------------------------------- | ------------- | ------------- | ----------------------------- |
ruby            | [json](https://rubygems.org/gems/json/versions/1.8.3)       | 101           | 202 bytes     |
rust            | [serde_json](https://docs.serde.rs/serde_json/)             | 128           | 256 bytes     |
php             | `json_decode`                                               | 512           | 1024 bytes    | maximum depth is configurable |
perl            | [JSON::PP](https://perldoc.perl.org/JSON/PP.html)           | 513           | 1026 bytes    |
python3         | [json](https://docs.python.org/3/library/json.html)         | 994           | 2.0 KB        | without sys.setrecursionlimit
C               | [jansson](https://jansson.readthedocs.io/)                  | 2049          | 4.0 KB        | 
java            | [Gson](https://github.com/google/gson)                      | 5670          | 11.3 KB       |
javascript      | `JSON.parse`                                                | 5713          | 11.4 KB       |
java            | [Jackson](https://github.com/FasterXML/jackson-core)        | 6373          | 13   KB       |
C++             | [nlohmann::json](https://github.com/nlohmann/json)          | 13787         | 27.6 KB       | segfault
Nim             | [json](https://nim-lang.org/docs/json.html)                 | 100000        | 200 KB        | w/ `-d:release`
go              | `encoding/json`                                             | 2581101       | 5.0 MiB       | goroutine stack exceeds 1000000000-byte limit
ruby            | [Oj](https://github.com/ohler55/oj)                         | ∞             | ∞             |
Haskell         | [Aeson](https://hackage.haskell.org/package/aeson)          | ∞             | ∞             | available RAM is the only limit
javascript      | [BFJ](https://www.npmjs.com/package/bfj)                    | ∞             | ∞             |


## Remarks

I tried to test the most popular json library of each language. If you want to add a new language or a new library,
feel free to open a pull request.

All the parameters were left to their default values. In particular, the result
for PHP is particular: `json_decode` accepts a `depth` parameter to configure
the maximum depth of the object to be parsed.
