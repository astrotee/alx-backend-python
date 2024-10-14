#!/usr/bin/env python3
"basics of async"
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    "wait for random range and return"
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
