# bad_json_parsers
Exposing problems in json parsers of several programming languages.

## Introduction

Many JSON parsers (and many parsers in general) use recursion to parse nested JSON structure.
This is very convenient while programming the parser, but it has consequenses on what the parser can parse:
indeed, the stack trace is usually limited to a value much smaller than the available RAM, and this implies
that a program with too many levels of recursion will fail.

However, the [JSON specification](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf)
doesn't contain any limit on how deeply nested JSON structures can be.
This means that most JSON parsers fail on a valid input.

This repository contains tools to measure the limits of JSON parsers of different languages.

## How to use

This repository contains a script called [test_parser.sh](test_parser.sh) that takes a JSON parser and uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest JSON structure it fails to parse and print its nesting level.

The json parser must be a program that reads JSON on its standard input, and exits with a status of 0 if it managed to parse it and any other status if an error occured.

## How it workd 

[test_parser.sh](test_parser.sh) constructs json structures composed uniquely of nested arrays, and gives them to the program it tests. For instance, for a depth of 3, it builds the following json : `[[[]]]`. This allows to create a structure of only *2n* bytes that has *n* nesting levels.
It uses [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) to find the smallest structure for which the programm fails.

## Results

On my machine (Ubuntu Linux 4.10.0-35-generic SMP x86_64 with 8Gb RAM), I found the following results:

language | json library                                                | nesting level | size of the JSON structure   |
-------- | ----------------------------------------------------------- | ------------- | ---------------------------- |
ruby     | [json](https://rubygems.org/gems/json/versions/1.8.3)       | 101           | 202 bytes                    |
python   | [json](https://docs.python.org/3/library/json.html)         | 994           | 2.0 kb                       | 
java     | [Gson](https://github.com/google/gson)                      | 5670          | 11.3 kb                      |
JS       | `JSON.decode`                                               | 5713          | 11.4 kb                      |

