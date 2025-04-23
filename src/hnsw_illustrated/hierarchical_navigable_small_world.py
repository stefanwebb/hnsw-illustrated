"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import Any, Dict, Iterable, List, Optional, Tuple

from hnsw_illustrated.graph import Node
from hnsw_illustrated.navigable_small_world import NavigableSmallWorld
import numpy as np

rng = np.random.default_rng(12345)


class HierarchicalNavigableSmallWorld:
    """
    Implements the HNSW method for vector space search
    """

    def __init__(
        self,
        count_layers: int = 5,
        config: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        # Each layer is a separate NSW
        # TODO: Call build from __init__?
        self._layers = [NavigableSmallWorld(config) for _ in range(count_layers)]

    def search(self, vector: np.array, width: int = 1) -> List[Tuple[float, Node]]:
        # TODO: raise exception is build hasn't been called yet
        pass

    def build(
        self,
        vectors: Iterable[np.array],
        p: float,  # probability for binomial distribution to sample layers
    ) -> None:
        # Sample all layer insertions at once
        layers = rng.binomial(p=p, size=len(vectors))

        # Do a 0-layer insert initially
        try:
            swap = np.where(layers == 0)[0]
            layers[swap], layers[0] = layers[0], layers[swap]
        except:
            layers[0] = 0

        # TODO: Difference between Iterator and Iterable
        for vector, layer in zip(vectors, layers):
            self._insert(vector, layer=layer)

    def _insert(self, vector, layer: int):
        pass


"""
    def _build_graph(self, config: Optional[List[Dict[str, Any]]]) -> None:
        # Iterate over nodes
        for n in self._nodes:
            assert not len(n.neighbors)

            # Find closest K-neighbors in graph built so far, starting from a random entry node

            # In practice, would repeat for multiple random entry nodes and merge results

            # TODO: Modify greedy_search to greedy_top_k

    def _greedy_top_k(self, target: Point, entry_node: Node, K: int = 5):
        candidates = MinHeap([entry_node])
        results = MaxHeap([entry_node])
        min_distance = distance(entry_node.data["pos"], target)

        while len(candidates):
            # Build top-K set until we have K to work with
            # if len(results) < K:
            #     results.push(closest_node)

            # Consider closest candidate...
            closest_node = candidates.pop()

            # ...to upper bound on top-K
            furthest_node = results[0]  # just peek at top

            # Find neighbors of candidate within top-K set
            max_distance = distance(furthest_node.data["pos"], target)
            for neighbor_node in closest_node.neighbors:
                neighbor_distance = distance(neighbor_node.data["pos"], target)
                if neighbor_distance < max_distance:
                    if len(results) > K:
                        results.pop()

                    results.push(neighbor_node)
                    candidates.push(neighbor_node)
                    max_distance = distance(results[0].data["pos"], target)

        return results

    def greedy_search(self, target: Point, entry_node: Node):
        closer_node = entry_node
        this_node = None
        while closer_node != this_node:  # or "is not"?
            min_distance = distance(closer_node.data["pos"], target)
            this_node = closer_node

            for node in this_node.neighbors:
                neighbor_distance = distance(node.data["pos"], target)
                if neighbor_distance < min_distance:
                    min_distance = neighbor_distance
                    closer_node = node

        return closer_node
"""
