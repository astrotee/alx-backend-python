#!/usr/bin/env python3
"basics of async"
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    "run wait_random n times and return them sorted"
    coros = [(wait_random(max_delay)) for _ in range(n)]
    return [await x for x in asyncio.as_completed(coros)]
