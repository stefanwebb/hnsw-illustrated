"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import Any, List

from hnsw_illustrated.graph import Graph

# from vedo import *
from vedo import Axes, np, Points, show, Lines, Arrows


def render_nsw(graph: "NavigableSmallWorld", z=0, c=(0.0, 1.0, 0.0)) -> List[Any]:
    # Render vertices
    vertices = graph.vertices()
    points = Points(
        np.concatenate([vertices, z * np.ones((len(vertices), 1))], axis=-1), r=8, c=c
    )

    # Render bidirectional edges
    edges = graph.bidirectional_edges()
    if len(edges) > 0:
        starts = np.concatenate([edges[:, 0, :], z * np.ones((len(edges), 1))], axis=-1)
        ends = np.concatenate([edges[:, 1, :], z * np.ones((len(edges), 1))], axis=-1)
        bidi_lines = Lines(starts, ends)
    else:
        bidi_lines = None

    # TODO: Render unidirectional edges
    edges = graph.unidirectional_edges()
    if len(edges) > 0:
        starts = np.concatenate([edges[:, 0, :], z * np.ones((len(edges), 1))], axis=-1)
        ends = np.concatenate([edges[:, 1, :], z * np.ones((len(edges), 1))], axis=-1)
        uni_lines = Lines(starts, ends, dotted=True, c=(1.0, 0.0, 0.0))
    else:
        uni_lines = None

    return [points, bidi_lines, uni_lines]


def render_hnsw(graph: "HierarchicalNavigableSmallWorld") -> List[Any]:
    stuff = []

    # Render vertices and edges for layers
    for idx, layer in enumerate(graph._layers):
        stuff.append(render_nsw(layer, z=len(graph._layers) - idx))

    # Render edges *between* layers
    down_edges = graph.down_edges()
    froms = down_edges[:, 0, :].tolist()
    tos = down_edges[:, 1, :].tolist()
    stuff.append(Lines(froms, tos, c=(0.1, 0.1, 0.1)))

    # more_stuff = []
    # for idx, layer in enumerate(graph._layers):

    return stuff  # + more_stuff


# TODO: Options
# TODO: Return Plotter?
# def render(graph: Graph) -> None:
#     pass
# for node in graph:
#     pass
# show(clpts, __doc__, axes=1, viewup="z", bg="blackboard").close()


def render(objs: List[Any]) -> None:
    axes = Axes(
        xrange=(-3.3, 3.3),
        yrange=(-3.3, 3.3),
        zrange=(1, 5),
    )

    show(*objs, axes, viewup="z", bg="white").close()
