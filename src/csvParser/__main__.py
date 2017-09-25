#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import memory_profiler
import profilehooks

from parser import csv_parser
from parser import split_parser


@profilehooks.timecall()
def csv_parser_time():
    print("\n\n\n- csv_parser_time()")
    csv_parser.travel_distance()


@memory_profiler.profile()
def csv_parser_memory():
    print("\n\n\n- csv_parser_memory()")
    csv_parser.travel_distance()


@profilehooks.timecall()
def split_parser_time():
    print("\n\n\n- split_parser_time()")
    split_parser.travel_distance()


@memory_profiler.profile()
def split_parser_memory():
    print("\n\n\n- split_parser_memory()")
    split_parser.travel_distance()


if __name__ == '__main__':
    csv_parser_time()
    split_parser_time()
    csv_parser_memory()
    split_parser_memory()
