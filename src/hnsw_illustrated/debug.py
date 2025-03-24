"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from src.hnsw_illustrated.graph import Graph
from src.hnsw_illustrated.node import Node

x_graph: Graph = Graph(
    [
        Node({"pos": (0, 0)}),  # 0
        Node({"pos": (1, 0)}),  # 1
        Node({"pos": (1, 1)}),  # 2
        Node({"pos": (0, 1)}),  # 3
        Node({"pos": (0.5, 0.5)}),  # 4
    ]
)

for idx in range(4):
    x_graph[idx].neighbors = set([x_graph[4]])

x_graph[4].neighbors = set([x_graph[idx] for idx in range(4)])
