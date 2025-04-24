"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import random
from typing import Any, Dict, List, Optional, Iterator, Set

from hnsw_illustrated.node import Node


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
