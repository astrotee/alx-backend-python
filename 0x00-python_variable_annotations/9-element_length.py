#!/usr/bin/env python3
"duck typing"
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    "return a tuple of each Sequence and its length"
    return [(i, len(i)) for i in lst]
