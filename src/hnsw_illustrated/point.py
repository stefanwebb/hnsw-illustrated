"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import math
from typing import Tuple

Point = Tuple[float, float]


def distance(point_a: Point, point_b: Point):
    ax, ay = point_a
    bx, by = point_b
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
