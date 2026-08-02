#!/usr/bin/env python3
"""Create asyncio tasks for random waits."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
