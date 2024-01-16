#!/usr/bin/env python3

import asyncio
import time

async_generator = __import__("0-async_generator").async_generator


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
    return result


print(f"TYPE: {type(print_yielded_values)}")
print(f"TYPE : {type(print_yielded_values())}")

s = time.perf_counter()
res = asyncio.run(print_yielded_values())
end = time.perf_counter()
print(f"end: {end}")
print(f"sum of res: {sum(res)}")
