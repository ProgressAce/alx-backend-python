#!/usr/bin/env python3
"""Defines a coroutine generator that loops 10 times."""

import asyncio
import random


async def async_generator() -> float:
    """Loops 10 times, and each time asynchronously waiting 1 second.

    Yield:
        a random floating point number between 0 and 10."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
