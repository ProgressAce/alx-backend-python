#!/usr/bin/env python3
"""Defines a function that _returns_ a function that multiplies a float."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable that multiplies a float by <multiplier>.

    Arg:
        multiplier(float): the float used to multiply another float.
    Returns:
        function <multiply_float>."""

    def multiply_float(x: float) -> float:
        """Multiplies a float by <multiplier>."""

        return multiplier * x

    return multiply_float
