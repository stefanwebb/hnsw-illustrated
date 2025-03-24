"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

from typing import Any, Dict, Set


class Node:
    def __init__(self, data: Dict[str, Any] = None, neighbors: Set["Node"] = set()):
        self.neighbors = neighbors
        self.data = data
