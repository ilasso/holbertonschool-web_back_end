#!/usr/bin/env python3
"""9-element_length: module to define function element_lenght"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
