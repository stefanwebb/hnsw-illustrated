"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import matplotlib.pyplot as plt
import numpy as np
import random
from hnsw_illustrated.navigable_small_world import NavigableSmallWorld


if __name__ == "__main__":
    # Dummy data
    rng = np.random.default_rng(12345)
    random.seed(12345)
    dataset = rng.normal(size=(12, 2))

    # Implement NavigableSmallWorld.search
    config = {"insert_width": 2, "max_neighbors": 5}
    nsw = NavigableSmallWorld(config=config)
    for x in dataset:
        nsw._insert(x)

    # print("total edges", nsw.count_edges)
    for node in nsw._nodes:
        print("node", hex(id(node)), "neighbors", len(node._neighbors))
        # print("neighbors ref", hex(id(node._neighbors)), node._neighbors)
        # print("\n")

    fig, ax = plt.subplots()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.scatter(dataset[:, 0], dataset[:, 1])

    # plot edges
    for node in nsw._nodes:
        # print(len(node._neighbors))
        for neighbor in node._neighbors:
            # edges must be bi-directional
            assert node in neighbor._neighbors

            x, y = node._data["vector"]
            nx, ny = neighbor._data["vector"]

            # if x < nx:
            ax.plot(
                [node._data["vector"][0], neighbor._data["vector"][0]],
                [node._data["vector"][1], neighbor._data["vector"][1]],
            )

    plt.show()

    """
        * Test HierarchicalNavigableSmallWorld.build
        * Test HierarchicalNavigableSmallWorld.search
        * Add default config to NSW / HNSW and create Config class
        * Visualizing graph building and search
    """
