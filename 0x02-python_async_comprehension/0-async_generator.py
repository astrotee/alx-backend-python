#!/usr/bin/env python3
"Async Comprehension"
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    "Async Generator"
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
