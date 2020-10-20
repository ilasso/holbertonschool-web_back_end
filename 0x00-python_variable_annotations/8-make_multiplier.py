#!/usr/bin/env python3
"""8-make_multiplier: module to define function sum_list"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier:
    return a function that multiplies a float by multiplier"""
    def freturn(a: float):
        """ freturn: return mult a floar by multiplier"""
        return a * multiplier
    return freturn
