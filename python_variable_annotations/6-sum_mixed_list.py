#!/usr/bin/env python3
"""Sum a list containing integers and floating-point values."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the values in ``mxd_lst``."""
    return sum(mxd_lst)
