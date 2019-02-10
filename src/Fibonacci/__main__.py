#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Benchmark tests for Fibonacci"""

import memory_profiler
import profilehooks

from src.packages.fibonacci import dynamic_programming
from src.packages.fibonacci import recursion


def main() -> None:
    """
    Main function to run this script

    :rtype: None
    """

    print("\n\n\n### Tests the maximum performance for recursion without memoization.")
    position = 40

    recursively_memory(position)
    memoization_memory(position)
    tabulation_memory(position)

    recursively_time(position)
    memoization_time(position)
    tabulation_time(position)

    recursively_profile(position)
    memoization_profile(position)
    tabulation_profile(position)

    print("\n\n\n### Tests the maximum performance for recursion with memoization.")
    position = 900

    memoization_memory(position)
    tabulation_memory(position)

    memoization_time(position)
    tabulation_time(position)

    memoization_profile(position)
    tabulation_profile(position)

    print("\n\n\n### Tests the maximum performance for dynamic programming.")
    position = 500000

    tabulation_memory(position)
    tabulation_time(position)
    tabulation_profile(position)


@profilehooks.timecall()
def recursively_time(n: int) -> None:
    """
    Run the benchmark for Fibonacci using recursion, it should recorded the total time.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.recursively(n)


@profilehooks.profile()
def recursively_profile(n: int) -> None:
    """
    Run the benchmark for Fibonacci using recursion, it should recorded the profile.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.recursively(n)


@memory_profiler.profile()
def recursively_memory(n: int) -> None:
    """
    Run the benchmark for Fibonacci using recursion, it should recorded the total used memory.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.recursively(n)


@profilehooks.timecall()
def memoization_time(n: int) -> None:
    """
    Run the benchmark for Fibonacci using memoization, it should recorded the total time.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.memoization(n)


@profilehooks.profile()
def memoization_profile(n: int) -> None:
    """
    Run the benchmark for Fibonacci using memoization, it should recorded the profile.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.memoization(n)


@memory_profiler.profile()
def memoization_memory(n: int) -> None:
    """
    Run the benchmark for Fibonacci using memoization, it should recorded the total used memory.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    recursion.memoization(n)


@profilehooks.timecall()
def tabulation_time(n: int) -> None:
    """
    Run the benchmark for Fibonacci using tabulation, it should recorded the total time.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    dynamic_programming.tabulation(n)


@profilehooks.profile()
def tabulation_profile(n: int) -> None:
    """
    Run the benchmark for Fibonacci using tabulation, it should recorded the profile.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    dynamic_programming.tabulation(n)


@memory_profiler.profile()
def tabulation_memory(n: int) -> None:
    """
    Run the benchmark for Fibonacci using tabulation, it should recorded the total used memory.

    :param n: Position that we are looking in the Fibonacci sequence.
    :rtype: None
    """
    dynamic_programming.tabulation(n)


if __name__ == '__main__':
    main()
