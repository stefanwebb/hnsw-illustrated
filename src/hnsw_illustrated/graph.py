"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import Any, Dict, List, Optional, Iterator, Set

from hnsw_illustrated.node import Node


class Graph:
    def __init__(
        self,
        nodes: Optional[Set[Node]] = None,
        config: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        self._config = config
        if nodes is not None:
            self._nodes = nodes
        else:
            self._nodes = set()

    # def __getitem__(self, idx: int) -> Any:
    #     return self._nodes[idx]

    def __iter__(self) -> Iterator[Node]:
        return iter(self._nodes)

    def top(self):
        """
        Get an arbitrary node but don't pop it
        """
        for node in self._nodes:
            return node

    # def __repr__(self) -> str:
    #     self.render()
    #     return "Graph()"

    # def __str__(self) -> str:
    #     self.render()
    #     return "Graph()"

    def add(self, node: Node) -> Node:
        if node in self._nodes:
            raise ValueError("cannot insert the same node twice")

        self._nodes.add(node)

        # TODO: Or return Graph?
        return node

    def _render(
        self,
    ) -> None:
        # TODO: Return a PyPlot graph object?
        # TODO: Visualize graph for debugging purposes
        pass
