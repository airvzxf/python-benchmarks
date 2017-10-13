#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""These are benchmarks test for CSV Parser.

This test compare two different ways for parse a CSV file.
The first is with the Python built-in module which is CSV and the other is with split built-in function.
Both ways are tested by two parameters, first the time to the script takes to finished the parser and the memory used.
"""

import travel

import memory_profiler
import profilehooks


@profilehooks.timecall()
def csv_parser_time():
    """Run the benchmark for CSV Parser and it should recorded the total time."""
    print("\n\n\n- csv_parser_time()")
    travel.csv_parser()


@memory_profiler.profile()
def csv_parser_memory():
    """Run the benchmark for CSV Parser and it should recorded the total used memory."""
    print("\n\n\n- csv_parser_memory()")
    travel.csv_parser()


@profilehooks.timecall()
def split_parser_time():
    """Run the benchmark for Split and it should recorded the total used memory."""
    print("\n\n\n- split_parser_time()")
    travel.split_parser()


@memory_profiler.profile()
def split_parser_memory():
    """Run the benchmark for Split and it should recorded the total used memory."""
    print("\n\n\n- split_parser_memory()")
    travel.split_parser()


if __name__ == '__main__':
    csv_parser_time()
    split_parser_time()
    csv_parser_memory()
    split_parser_memory()
