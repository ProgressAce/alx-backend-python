#!/usr/bin/env python3
"""Defines a function that sums a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats.

    Arg:
        input_list(list of floats): a list containing float numbers."""

    total: float = 0

    for num in input_list:
        total += num

    return total
