#!/usr/bin/env python3
"""Defines an async coroutine that waits returns a random float number."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random amount of seconds, between 0 and max_delays.

    max_delay(int): the included upper range of the random wait time.

    Returns:
        the waiting time."""

    waiting_time = random.uniform(0, max_delay)

    # pause current coroutine until task finishes
    await asyncio.sleep(waiting_time)
    return waiting_time
