#!/usr/bin/env python
# coding=utf-8
"""
Compare different solutions for Fibonacci.
It's the classic recursion.
"""


def recursively(n: int) -> int:
    """
    This method get the fibonacci number at some specific position.
    It shows the slowly solution for this fibonacci using recursion which is O(n2).

    :param n: Fibonacci position that you're looking.
    :rtype: int
    :return: The Fibonacci number.
    """
    if n == 1 or n == 2:
        result = 1
    else:
        result = recursively(n - 1) + recursively(n - 2)

    return result
