#!/usr/bin/env python
# -*- encoding: utf8 -*-

from __future__ import print_function, unicode_literals

import logging
import subprocess
import sys

assert sys.version_info >= (2, 7), "Requires python >= 2.7 to run"

MIN_NESTING = 1
MAX_NESTING = 5000000

assert len(sys.argv) >= 2, "Not enough arguments"
program = sys.argv[1:]

NESTED_ARRAYS = b'[' * MAX_NESTING + b']' * MAX_NESTING

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)-15s %(funcName)s] %(message)s')
log = logging.getLogger(__name__)


def print_bytes(b, out):
    max_out_len = 5000
    if len(b) > max_out_len:
        b = b[:max_out_len // 2] + b'\n[...]\n' + b[-max_out_len // 2:]
    buffer = getattr(out, 'buffer', out)
    buffer.write(b)
    buffer.flush()


def deep_json_array(depth):
    m = len(NESTED_ARRAYS) // 2
    return NESTED_ARRAYS[m - depth:m + depth]


def run_program(depth, log_output=False):
    log.info("Launching {}".format(program))
    proc = subprocess.Popen(
        args=program,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    log.info("Writing {} nested arrays".format(depth))
    stdout, stderr = proc.communicate(deep_json_array(depth))

    log.info('Command exited with {}'.format(proc.returncode))
    if log_output and stdout:
        log.info("Program's stdout:")
        print_bytes(stdout, out=sys.stdout)
    if log_output and stderr:
        log.info("Program's stderr:")
        print_bytes(stderr, out=sys.stdout)
    return proc.returncode == 0


def binary_search(f, start, end):
    while end != start + 1:
        middle = (start + end) // 2
        if f(middle):
            start = middle
        else:
            end = middle
    return end


def main():
    if not run_program(MIN_NESTING, log_output=True):
        print("Cannot apply a binary search. "
              "Input program failed even with an input of {}".format(MIN_NESTING),
              file=sys.stderr)
        return 1
    if run_program(MAX_NESTING, log_output=True):
        print("∞")
        return 0
    min_failing_depth = binary_search(
        run_program,
        start=MIN_NESTING,
        end=MAX_NESTING)
    log.info(("The shortest valid JSON payload that cannot be parsed by "
              "{} is {} levels deep "
              "and weighs {:.1f} kB"
              ).format(' '.join(program), min_failing_depth, min_failing_depth * 2 / 1000))
    print(min_failing_depth)
    return 0


if __name__ == "__main__":
    exit(main())
