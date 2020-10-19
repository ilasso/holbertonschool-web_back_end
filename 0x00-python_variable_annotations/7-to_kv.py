#!/usr/bin/env python3
"""7-to_kv: module to define function to_kv"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: return tuple, (str,float)"""

    return (k, float(v*v))
