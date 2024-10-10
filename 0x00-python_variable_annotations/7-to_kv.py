#!/usr/bin/env python3
"complex types"
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "string and int/float to tuple"
    return (k, v**2)
