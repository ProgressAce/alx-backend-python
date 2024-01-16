#!/usr/bin/env python3

import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def main():
    """asynchronous top-level entry point."""
    print(await async_comprehension())


asyncio.run(main())
