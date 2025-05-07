"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from copy import copy
from typing import Any, Dict, List, Optional, Tuple

from hnsw_illustrated.binary_heap import MaxHeap, MinHeap
from hnsw_illustrated.graph import Graph, Node
from hnsw_illustrated.metrics import l2_distance
import numpy as np


# done_this = False


class NavigableSmallWorld(Graph):
    """
    Implements a basic navigable small world search index
    """

    def __init__(self, config: Optional[List[Dict[str, Any]]] = None):
        # TODO: Pass in distance metric
        super().__init__(nodes=None, config=config)

    # TODO: build method in case want to compare with HNSW
    # def build(self, ...)

    def _insert(
        self,
        vector: np.array,
        entry_node: Optional[Node] = None,
        shrink_neighborhoods: bool = False,
    ) -> Node:
        if entry_node is None:
            entry_node = self.random()

        # Calculate neighbors of new node from greedy search
        neighbors = set(
            [
                n
                for _, n in self.search(
                    vector, entry_node, self._config["insert_width"]
                )
            ]
        )

        node = Node({"vector": vector}, neighbors)

        # Connect neighbors of new node to node
        for neighbor in neighbors:
            neighbor.connect(node)

            # Shrink neighbor's neighborhood if necessary
            """if (
                shrink_neighborhoods
                and len(neighbor.neighbors) > self._config["max_neighbors"]
            ):
                # Find new neighbors
                dists = sorted(
                    [
                        (l2_distance(neighbor.vector, nn.vector), nn)
                        for nn in neighbor.neighbors
                    ]
                )
                neighbor_neighbors = [
                    n for _, n in dists[: self._config["max_neighbors"]]
                ]

                # Disconnect the old and reconnect the new
                old_neighbors = copy(neighbor.neighbors)

                neighbor.disconnect_all()
                neighbor.connect_all(neighbor_neighbors)"""

        self.add(node)
        return node

    def search(
        self, query: np.array, entry_node: Optional[Node] = None, width: int = 1
    ) -> List[Tuple[float, Node]]:
        if entry_node is None:
            entry_node = self.random()
            if entry_node is None:
                return []

        visited = set([entry_node])
        distance = l2_distance(query, entry_node.vector)
        candidates = MinHeap([(distance, entry_node)])
        top_k = MaxHeap([(distance, entry_node)])

        # Greedy search
        while len(candidates):
            candidate = candidates.pop()

            # Finish if current top-K's maximum distance to query
            # is less than current candidates minimum distance to query
            if top_k.top()[0] < candidate[0]:
                break

            # loop through all nearest neighbors to the candidate vector
            # cv[1] is list of neighbor indices to min element
            # graph[cv[1]][1] is neighbors of cv[1]
            for neighbor in candidate[1].neighbors:
                # Calculate distance of this neighbor to query
                dist = l2_distance(neighbor.vector, query)

                # If we haven't visited this node before...
                if neighbor not in visited:
                    visited.add(neighbor)

                    # push only "better" vectors into candidate heap
                    if dist < top_k.top()[0] or len(top_k) < width:
                        # add this node to candidate min-heap
                        candidates.push((dist, neighbor))

                        # insert element into sorted list of top-K results
                        top_k.push((dist, neighbor))

                        # if we have added (K+1) result then remove largest one
                        if len(top_k) > width:
                            top_k.pop()

        # Do heapsort to sort top-k from closest to furthest
        return list(reversed(top_k.sort()))
