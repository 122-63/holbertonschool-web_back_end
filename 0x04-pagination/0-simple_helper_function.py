#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page, page_size):
    """
        Range of the page
        Args:
            page: Current page
            page_size: Total size of the page
        Return:
            tuple with the range start and end size page
    """

    if page and page_size:
        start_size = (page - 1) * page_size
        final_size = start_size + page_size
        return start_size, final_size
