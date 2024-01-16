#!/usr/bin/env python3
"""Defines a coroutine that obtains the values from an async iterable."""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """Uses async omprehension to obtain the values from async_generator."""

    async_generator_values = [num async for num in async_generator()]
    return async_generator_values
