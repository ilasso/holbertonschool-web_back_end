#!/usr/bin/env python3
"""6-sum_mixed_list: module to define function sum_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list: return sum of all elements(floats)"""
    return sum(mxd_lst)
