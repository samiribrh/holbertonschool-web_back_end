#!/usr/bin/env python3
"""Module for function that creates mixed tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of k and v square"""
    return k, float(pow(v, 2))
