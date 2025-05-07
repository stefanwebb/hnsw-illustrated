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
        super().__setattr__("neighbors", neighbors)
        super().__setattr__("data", data)

    def __repr__(self):
        return self._str()

    def __str__(self):
        return self._str()

    def _str(self):
        neighbors = ", ".join([f"{n.vector}" for n in self.neighbors])
        return f"Node(\n\tNeighbors: {neighbors}\n\tData: {self.data}\n)\n"

    def __getattr__(self, key):
        if key in ["neighbors", "data"]:
            return super().getattr(key)

        try:
            return self.data[key]
        except KeyError:
            # More graceful failure behavior
            return None
            # raise AttributeError(f"'Node' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        if key == "neighbors":
            raise AttributeError(f"Cannot set neighbors attribute of 'Node'")

        self.data[key] = value

    def connect(self, node: "Node") -> "Node":
        self.neighbors.add(node)
        node.neighbors.add(self)
        return self

    def connect_all(self, nodes: Iterable["Node"]) -> "Node":
        for node in nodes:
            self.connect(node)
        return self

    def disconnect(self, node: "Node") -> "Node":
        self.neighbors.discard(node)
        node.neighbors.discard(self)

    def disconnect_all(self, nodes: Optional[Iterable["Node"]] = None) -> "Node":
        if nodes is None:
            nodes = copy(self.neighbors)

        for node in nodes:
            self.disconnect(node)
        return self
