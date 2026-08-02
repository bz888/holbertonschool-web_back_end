#!/usr/bin/env python3
"""Create a floating-point multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by ``multiplier``."""
    def multiply(value: float) -> float:
        """Multiply ``value`` by the enclosing multiplier."""
        return value * multiplier

    return multiply
