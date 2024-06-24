#!/usr/bin/python3
"""
Pagination Task 0: simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function returnong the start, end index of pages"""

    start_idx = 0

    for i in range(1, page):
        start_idx += page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)
