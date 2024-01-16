#!/usr/bin/env python3
"""Defines a coroutine generator that loops 10 times."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, and each time asynchronously waiting 1 second.

    Yield:
        a random floating point number between 0 and 10."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
