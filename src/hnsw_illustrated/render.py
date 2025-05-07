"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from hnsw_illustrated.graph import Graph
from hnsw_illustrated.hierarchical_navigable_small_world import (
    HierarchicalNavigableSmallWorld,
)

# from vedo import *
from vedo import np, Points, show

# Generate 4 random sets of N points in 3D space
N = 2000
f = 0.6
# noise1 = np.random.rand(N, 3) * f + np.array([1, 1, 0])
# noise2 = np.random.rand(N, 3) * f + np.array([1, 0, 1.2])
# noise3 = np.random.rand(N, 3) * f + np.array([0, 1, 1])
# noise4 = np.random.randn(N, 3) * f / 8 + np.array([1, 1, 1])

# Create a Points object from the noisy point sets
noise4 = Points(noise4).remove_outliers(radius=0.05).coordinates

pts = noise1.tolist() + noise2.tolist()
pts = Points(pts, c=(1.0, 1.0, 1.0))

pts2 = noise3.tolist() + noise4.tolist()
pts2 = Points(pts2, c=(0, 1.0, 1.0))

# Cluster the points to find back their original identity
# clpts = pts.compute_clustering(radius=0.1).print()
# Set the color of the points based on their cluster ID using the 'jet' colormap
# clpts.cmap("jet", "ClusterId")

show(pts, pts2, __doc__, axes=1, viewup="z", bg="blackboard").close()


def render_hnsw(graph: HierarchicalNavigableSmallWorld) -> None:
    layer_ptr = [Points(layer.vertices, c=(0.5, 0.0, 0.5)) for layer in graph._layers]


# TODO: Options
# TODO: Return Plotter?
# def render(graph: Graph) -> None:
#     pass
# for node in graph:
#     pass
# show(clpts, __doc__, axes=1, viewup="z", bg="blackboard").close()
