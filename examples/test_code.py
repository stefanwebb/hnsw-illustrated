"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import numpy as np
from hnsw_illustrated.navigable_small_world import NavigableSmallWorld


if __name__ == "__main__":
    # Dummy data
    dataset = np.random.normal(size=(1000, 128))

    # Implement NavigableSmallWorld.search
    config = {
        "insert_width": 5,
    }
    nsw = NavigableSmallWorld(config=config)
    for x in dataset[0:2]:
        nsw._insert(x)

    """
        * Test HierarchicalNavigableSmallWorld.build
        * Test HierarchicalNavigableSmallWorld.search
        * Add default config to NSW / HNSW and create Config class
        * Visualizing graph building and search
    """
