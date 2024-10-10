#!/usr/bin/env python3
"Complex types"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "return a Callable"
    return lambda x: x*multiplier
