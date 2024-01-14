#!/usr/bin/env python3
"""Defines a function that sums a mixed list of int and floats."""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Returns the sum of all the elements in <mxd_lst>.

    Arg:
        mxd_lst(list of int,float): list of integers and floats.

    Returns:
        the sum of <mxd_lst>'s elements as a float."""

    total: float = 0

    for num in mxd_lst:
        total += num

    return total
