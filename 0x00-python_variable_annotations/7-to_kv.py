#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: String
            v: Union: Can be int or float
        Return:
            Tuple with string and int or float
    """

    cncat: Tuple(str, Union[int, float])
    cncat = (k, v**2)

    return cncat
