#!/usr/bin/env python3
"""Collect values from an asynchronous generator."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 values collected with an async comprehension."""
    return [number async for number in async_generator()]
