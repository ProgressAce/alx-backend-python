#!/usr/bin/env python3

import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def test(max_delay: int) -> float:
    """Tests <task_wait_random> return value."""
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


asyncio.run(test(5))
