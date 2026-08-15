#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset without its header row."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by its original position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page based on stable dataset indexes."""
        indexed_dataset = self.indexed_dataset()
        assert index is not None and index in indexed_dataset
        assert type(page_size) is int and page_size > 0

        data = [
            indexed_dataset[item_index]
            for item_index in range(index, index + page_size)
            if item_index in indexed_dataset
        ]

        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": len(data),
            "data": data,
        }
