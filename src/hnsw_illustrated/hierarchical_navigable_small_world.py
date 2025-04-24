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

        # TODO: Difference between Iterator and Iterable?
        for vector, layer in zip(vectors, layers):
            self._insert(vector, layer=layer)

    def _insert(self, vector, layer_idx: int):
        # first phase is to navigate down and find entry point
        entry_node = self._layer[layer_idx].random()
        for this_idx in range(0, layer_idx):
            # find closest match at each layer
            entry_node = self._layers[this_idx].search(vector, entry_node)[0]

        # second phase does insertion
        previous_node = None
        for this_idx in range(layer_idx, len(self._layers)):
            # insert at each layer and connect to next layer
            node = self._layers[this_idx]._insert(
                vector, entry_node, shrink_neighborhoods=True
            )
            if previous_node:
                previous_node._data["down"] = node
            previous_node = node
