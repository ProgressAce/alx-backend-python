#!/usr/bin/env python3
"""Defines a function that returns a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Returns a tuple of a string and the square of v as a float.

    Args:
        k(str): a string.
        v(int | float): the int or float to square."""

    power_2: float = v * v

    return (k, power_2)
