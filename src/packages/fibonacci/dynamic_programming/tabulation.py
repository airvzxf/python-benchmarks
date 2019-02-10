#!/usr/bin/env python
# coding=utf-8
"""
Compare different solutions for Fibonacci.
It's the dynamic programming method with tabulation which is know as bottom-up.
"""


def tabulation(n: int) -> int:
    """
    This method get the fibonacci number at some specific position.
    It shows the faster solution for this fibonacci which is O(n).

    :param n: Fibonacci position that you're looking.
    :rtype: int
    :return: The Fibonacci number.
    """
    if n == 1 or n == 2:
        return 1

    bottom_up = [0] + [1] + [1] + [0] * (n - 2)

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    return bottom_up[n]
