#!/usr/bin/env python3
"""Defines an async coroutine that calls wait_random n times."""

import asyncio
import time
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random <n> times.

    Args:
        n: the number of times to call wait_random.
        max_delay: the included upper range argument to give wait_random.

    Returns:
        a list of floats indicating all the wait times from every called
        wait_random coroutine."""

    wait_times: List[float] = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )

    return wait_times
