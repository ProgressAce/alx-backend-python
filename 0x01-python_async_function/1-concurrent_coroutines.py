#!/usr/bin/env python3
"""Defines an async coroutine that calls wait_random n times."""

import asyncio
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

    wait_times: List[float] = []

    import time

    task_list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    s = time.perf_counter()
    # for _ in range(n):
    # only one coroutine in event loop so it will execute only the one
    # coroutine as there are no other existing coroutines to give
    # control to, while waiting for wait_random
    # delay = await wait_random(max_delay)

    # put coroutine in event loop
    # task = asyncio.create_task(wait_random(max_delay))
    # task_list.append(task)

    for task in task_list:
        delay = await task
        print(delay)
        wait_times.append(delay)

    end = time.perf_counter() - s
    print(end)
    # await asyncio.gather(
    #    *(wait_random(max_delay) for _ in range(n))
    # )

    return wait_times
