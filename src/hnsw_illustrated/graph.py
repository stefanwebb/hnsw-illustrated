"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import List

from src.hnsw_illustrated.node import Node
from src.hnsw_illustrated.point import Point, distance


class Graph:
    def _init__(self, nodes: List[Node] = []):
        self._nodes = nodes

    def __getitem__(self, idx):
        return self._nodes[idx]

    def __iter__(self):
        return iter(self._nodes)

    # TODO: Visualize graph for debugging purposes
    def __repr__(self):
        self.render()

    def __str__(self):
        self.render()

    def greedy_search(self, target: Point, entry_node: Node):
        results = []
        closer_node = entry_node
        while closer_node is not None:
            min_distance = distance(closer_node.data["pos"], target)
            this_node, closer_node = closer_node, None

            for node in this_node.neighbors:
                neighbor_distance = distance(entry_node.data["pos"], node.data["pos"])
                if neighbor_distance < min_distance:
                    min_distance = neighbor_distance
                    closer_node = node

        return results
