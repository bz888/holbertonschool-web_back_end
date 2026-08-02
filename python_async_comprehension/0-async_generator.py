#!/usr/bin/env python3
"""Define an asynchronous random-number generator."""

import asyncio
import random


async def async_generator():
    """Yield 10 random numbers, waiting one second before each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
