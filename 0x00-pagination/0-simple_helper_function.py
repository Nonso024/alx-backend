#!/usr/bin/env/python3
""" This module adds indexes to pages """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ An tuple conatining start and end index is returned """

    front = (page - 1) * page_size
    back = front + page_size
    return (front, backu)
