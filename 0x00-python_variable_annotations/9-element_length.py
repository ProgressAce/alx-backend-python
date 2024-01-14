#!/usr/bin/env python3
"""Annotates the below function the appropriate types."""

from typing import Iterator, Sequence


def element_length(lst: Iterator[Sequence]) -> list[tuple[Sequence, int]]:
    """Returns each element's length and value in tuple form.

    Arg:
        lst(Iterator): An iteratable of iterables.
    Returns:
        a list of tuples of each element's length in <lst>."""

    return [(i, len(i)) for i in lst]
