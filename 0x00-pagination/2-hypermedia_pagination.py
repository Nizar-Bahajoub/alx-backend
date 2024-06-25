#!/usr/bin/env python3
"""Pagination Task 1: Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function returnong the start, end index of pages
    """

    start_idx = 0

    for i in range(1, page):
        start_idx += page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Getting page content Base On Start and end indexes
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        start, end = index_range(page, page_size)
        if 0 <= start < len(self.dataset()) and 0 <= end < len(self.dataset()):
            return self.dataset()[start:end]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retruns a dictionary containing the principlaes keys
        """
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': page + 1 if end < len(self.__dataset) else None,
                'prev_page': page - 1 if start > 1 else None,
                'total_pages': total_pages
                }
