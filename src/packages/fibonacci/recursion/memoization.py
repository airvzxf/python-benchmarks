#!/usr/bin/env python
# coding=utf-8
"""
Compare different solutions for Fibonacci.
It's the recursion method with memoization which is know as top-down.
"""


def memoization(n: int, memo: list = None) -> int:
    """
    This method get the fibonacci number at some specific position.
    It shows the fast solution for this fibonacci using recursion which is O(n).

    :param n: Fibonacci position that you're looking.
    :param memo: It's a list with
    :rtype: int
    :return: The Fibonacci number.
    """
    if memo is None:
        memo = {}

    if memo.get(n):
        return memo[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = memoization(n - 1, memo) + memoization(n - 2, memo)

    memo[n] = result
    return result
