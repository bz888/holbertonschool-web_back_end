#!/usr/bin/env python3
"""Create a key/value tuple with a squared numeric value."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return ``k`` paired with the square of ``v``."""
    return (k, v ** 2)
