#!/usr/bin/env python3
"""Defines a coroutine that measures coroutine <async_comprehension>"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """Executes coroutine <async_comprehension> 4 times and measures its
    total runtime.

    Returns:
        the total runtime."""

    coroutines = [async_comprehension() for _ in range(4)]

    start: float = time.perf_counter()
    await asyncio.gather(*coroutines)
    runtime: float = time.perf_counter() - start

    return runtime
