"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import random
from typing import Any, Dict, List, Optional, Iterator, Set, Tuple

from hnsw_illustrated.node import Node
import numpy as np


class Graph:
    def __init__(
        self,
        nodes: Optional[List[Node]] = None,
        config: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        self._config = config
        if nodes is not None:
            self._nodes = nodes
        else:
            self._nodes = []

    # def __getitem__(self, idx: int) -> Any:
    #     return self._nodes[idx]

    def __iter__(self) -> Iterator[Node]:
        return iter(self._nodes)

    # def __repr__(self) -> str:
    #     self.render()
    #     return "Graph()"

    # def __str__(self) -> str:
    #     self.render()
    #     return "Graph()"


    def vertex_iter(self):
        for node in self:
            if node.pos:
                yield node.pos

    def vertices(self) -> np.array:
        return np.array(list(self.vertex_iter()))

    def edge_iter(self):
        for node in self:
            if not node.pos:
                continue

            for neighbor in node.neighbors:
                if not neighbor.pos:
                    continue

                yield (node.pos, neighbor.pos)

    def edges(self) -> np.array:
        return np.array(list(self.edge_iter()))

    def count_edges(self) -> Dict[Tuple[float, float], int]:
        cts = {}

        for pos_from, pos_to in self.edge_iter():
            if pos_to < pos_from:
                pos_to, pos_from = pos_from, pos_to
            cts.my_dict.setdefault((pos_from, pos_to), 0) += 1

        return cts

    def bidirectional_edges(self) -> np.array:
        return np.array([val for key, val in self.count_edges() if val == 2])

    def unidirectional_edges(self) -> np.array:
        return np.array([val for key, val in self.count_edges() if val == 1])

    def random(self) -> Optional[Node]:
        if not len(self._nodes):
            return None

        return self._nodes[random.randrange(0, len(self._nodes))]

    def add(self, node: Node) -> Node:
        self._nodes.append(node)

        # TODO: Or return Graph?
        return node

    def _render(
        self,
    ) -> None:
        # TODO: Return a PyPlot graph object?
        # TODO: Visualize graph for debugging purposes
        pass
