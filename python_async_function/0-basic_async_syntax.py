#!/usr/bin/env python3
"""Module for basic async syntax example."""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10):
    """Wait a random number between 0 and max_delay."""
    wait_time = uniform(0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
