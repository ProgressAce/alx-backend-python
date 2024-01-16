#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def main():
    """asynchronous top-level entry point."""
    print(await async_comprehension())


s = time.perf_counter()
asyncio.run(main())
end = time.perf_counter() - s
print(end)
