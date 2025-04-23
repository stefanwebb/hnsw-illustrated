"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import Any, Dict, Set


class Node:
    def __init__(self, data: Dict[str, Any] = None, neighbors: Set["Node"] = set()):
        self._neighbors = neighbors
        self._data = data

    def __repr__(self):
        return self._str()

    def __str__(self):
        return self._str()

    def _str(self):
        neighbors = ", ".join([f'{n._data["pos"]}' for n in self._neighbors])
        return f"Node(\n\tNeighbors: {neighbors}\n\tData: {self.data}\n)\n"

    def connect(self, node: "Node") -> "Node":
        self._neighbors.add(node)
        node._neighbors.add(self)
        return self
