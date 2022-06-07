#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst: Sequence of list
        Return:
            List of tuple of sequence of integers
    """

    return [(i, len(i)) for i in lst]
