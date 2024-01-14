#!/usr/bin/env python3
"""Annotates the below function the appropriate types."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns each element's length and value in tuple form.

    Arg:
        lst(Iterator): An iteratable of iterables.
    Returns:
        a list of tuples of each element's length in <lst>."""

    return [(i, len(i)) for i in lst]
