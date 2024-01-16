#!/usr/bin/env python3
"""Main file for testing 0-basic_async_syntax.py"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

print(type(asyncio.run(wait_random())))
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

# additional
print(asyncio.run(wait_random(-10)))
print(asyncio.run(wait_random(2.5)))
