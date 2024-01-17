#!/usr/bin/env python3
"""Defines a coroutine that obtains the values from an async iterable."""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Uses async omprehension to obtain the values from async_generator."""

    generator_values: List[float] = [num async for num in async_generator()]
    return generator_values
