"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time

from hnsw_illustrated.hierarchical_navigable_small_world import (
    HierarchicalNavigableSmallWorld,
)
from hnsw_illustrated.navigable_small_world import NavigableSmallWorld
from hnsw_illustrated.render import render, render_nsw
from vedo import show, Axes, Plotter, Video

if __name__ == "__main__":
    # Dummy data
    rng = np.random.default_rng(12345)
    random.seed(12345)
    dataset = rng.normal(size=(100, 2))

    config = {"insert_width": 2, "max_neighbors": 5}
    nsw = NavigableSmallWorld(config=config)

    plt = Plotter()
    axes = Axes(
        xrange=(-3.3, 3.3),
        yrange=(-3.3, 3.3),
        zrange=(1, 5),
    )

    video = Video("build-nsw.mp4", backend="ffmpeg")
    for step_stuff in nsw.build_yield(dataset):
        # render(step_stuff)

        plt.show(
            *step_stuff,
            axes,
            viewup="z",
            bg="white",
            camera={"pos": (0, 0, 15)},
            interactive=False,
        )
        video.add_frame()

        # show(step_stuff[0], viewup="z")
        # plt.show(step_stuff, viewup="z")
        # plt.render()

        time.sleep(0.1)
        plt.clear()
        # break

    # video.action()
    video.close()
    plt.close()

    # plt.interactive().close()

    # stuff = render_nsw(nsw, z=0)
    # show(*stuff, axes=1, viewup="z", camera={"pos": (0, 0, 15)}, bg="white").close()

    # Build search structure
    # config = {"insert_width": 2, "max_neighbors": 5}
    # hnsw = HierarchicalNavigableSmallWorld(config=config)
    # hnsw.build(dataset, 0.5)

    # stuff = render_nsw(nsw, z=1)
    # stuff2 = render_nsw(nsw, z=0, c=(0, 0, 1))
    # show(*stuff, *stuff2, axes=1, viewup="z", bg="white").close()

    # DEBUG: Test edge, vertex methods on Graph
    # print("individual vertices")
    # for vertex in nsw.vertex_iter():
    #     print(vertex)

    # print("\nvertex array\n", nsw.vertices())

    # print("edges")
    # for edge in nsw.edge_iter():
    #     print(edge)

    # print(len(nsw.edges()))

    # print("\n\n")
    # print("uni-directional edges")
    # print(nsw.unidirectional_edges())

    # print("\n\n")
    # print("bi-directional edges")
    # print(nsw.bidirectional_edges())

    # print(len(nsw.bidirectional_edges()))

    """
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

    """
        * Test HierarchicalNavigableSmallWorld.build
        * Test HierarchicalNavigableSmallWorld.search
        * Add default config to NSW / HNSW and create Config class
        * Visualizing graph building and search
    """
