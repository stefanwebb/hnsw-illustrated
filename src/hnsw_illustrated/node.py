"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from copy import copy
from typing import Any, Dict, Iterable, Optional, Set


class Node:
    def __init__(self, data: Dict[str, Any] = None, neighbors: Set["Node"] = set()):
        self._neighbors = neighbors
        self._data = data

    def __repr__(self):
        return self._str()

    def __str__(self):
        return self._str()

    def _str(self):
        neighbors = ", ".join([f'{n._data["vector"]}' for n in self._neighbors])
        return f"Node(\n\tNeighbors: {neighbors}\n\tData: {self._data}\n)\n"

    def connect(self, node: "Node") -> "Node":
        self._neighbors.add(node)
        node._neighbors.add(self)
        return self

    def connect_all(self, nodes: Iterable["Node"]) -> "Node":
        for node in nodes:
            self.connect(node)
        return self

    def disconnect(self, node: "Node") -> "Node":
        self._neighbors.discard(node)
        node._neighbors.discard(self)

    def disconnect_all(self, nodes: Optional[Iterable["Node"]] = None) -> "Node":
        if nodes is None:
            nodes = copy(self._neighbors)

        for node in nodes:
            self.disconnect(node)
        return self
