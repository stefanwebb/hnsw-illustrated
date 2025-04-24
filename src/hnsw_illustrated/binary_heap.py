"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from enum import Enum
from heapq import heapify, heappop, heappush
from heapq_max import heapify_max, heappop_max, heappush_max
from typing import Any, List, Optional


class HeapType(Enum):
    MIN_HEAP = True
    MAX_HEAP = False


class BinaryHeap:
    """
    Binary heap (either min-heap or max-heap) that wraps Python's `heapq` library and PyPI `heapq_max` library
    """

    def __init__(
        self, data: Optional[List[Any]] = None, heap_type: HeapType = HeapType.MIN_HEAP
    ) -> None:
        self._heap_type = heap_type

        if data is not None:
            self._data = data
            if self.is_min_heap:
                heapify(self._data)
            else:
                heapify_max(self._data)

        else:
            self._data = []

    def __getitem__(self, idx: int) -> Any:
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def is_min_heap(self):
        return self._heap_type.value

    def sort(self) -> List[Any]:
        # Destructive heapsort
        ans = []
        while len(self):
            ans.append(self.pop())

        return ans

    def pop(self) -> Any:
        """
        Remove and return top element, maintaining heap property in O(log(n))
        """
        if self.is_min_heap():
            return heappop(self._data)
        else:
            return heappop_max(self._data)

    def push(self, x: Any) -> None:
        """
        Insert element and maintain heap property in O(log(n))
        """
        if self.is_min_heap():
            return heappush(self._data, x)
        else:
            return heappush_max(self._data, x)

    def top(self) -> Any:
        """
        Return the min element of min-heap or max element of max-heap in O(1)
        """
        return self[0]

    def bottom(self) -> Any:
        """
        Return the max element of min-heap or min element of max-heap in O(N)
        """
        # Due to heap property, ans must be a leaf node
        # TODO: find min/max of leaf nodes
        pass

    def leaves(self) -> Any:
        # TODO: return leaf nodes as slice
        pass


class MinHeap(BinaryHeap):
    def __init__(self, data: Optional[List[Any]] = None) -> None:
        super().__init__(data, HeapType.MIN_HEAP)


class MaxHeap(BinaryHeap):
    def __init__(self, data: Optional[List[Any]] = None) -> None:
        super().__init__(data, HeapType.MAX_HEAP)
