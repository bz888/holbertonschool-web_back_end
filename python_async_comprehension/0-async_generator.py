#!/usr/bin/env python3
"""Define an asynchronous random-number generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random numbers, waiting one second before each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
