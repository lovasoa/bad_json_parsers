#!/usr/bin/env python3

import asyncio
import logging
import sys

assert sys.version_info >= (3, 5), "Requires python >= 3.5 to run"

MIN_NESTING = 1
MAX_NESTING = 5_000_000

assert len(sys.argv) >= 2, "Not enough arguments"
[_, program, *arguments] = sys.argv

NESTED_ARRAYS = b'[' * MAX_NESTING + b']' * MAX_NESTING

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)-15s %(funcName)s] %(message)s')
log = logging.getLogger(__name__)


def deep_json_array(depth):
    m = len(NESTED_ARRAYS) // 2
    return NESTED_ARRAYS[m - depth:m + depth]


async def run_program(depth, log_output=False):
    log.info(f"Launching {program}")
    proc = await asyncio.create_subprocess_exec(
        program, *arguments,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    log.info(f"Writing {depth} nested arrays")
    proc.stdin.write(deep_json_array(depth))
    proc.stdin.close()
    stdout, stderr = await proc.communicate()

    log.info(f'Command exited with {proc.returncode}')
    if log_output and stdout:
        log.info(f"Program's stdout:")
        sys.stderr.buffer.write(stdout)
    if log_output and stderr:
        log.info(f"Program's stderr:")
        sys.stderr.buffer.write(stderr)
    return proc.returncode == 0


async def binary_search(f, start, end):
    while not (end == start + 1):
        middle = (start + end) // 2
        if await f(middle):
            start = middle
        else:
            end = middle
    return end


async def main():
    if not await run_program(MIN_NESTING, log_output=True):
        print(f"Cannot apply a binary search. "
              f"Input program failed even with an input of {MIN_NESTING}", file=sys.stderr)
        return 1
    if await run_program(MAX_NESTING, log_output=True):
        print("∞")
        return 0
    min_failing_depth = await binary_search(
        run_program,
        start=MIN_NESTING,
        end=MAX_NESTING)
    log.info("The shortest valid JSON payload that cannot be parsed by "
             f"{program} is {min_failing_depth} levels deep "
             f"and weighs {min_failing_depth * 2 / 1000:.1f} kB")
    print(min_failing_depth)
    return 0


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    status = loop.run_until_complete(main())
    loop.close()
    exit(status)
