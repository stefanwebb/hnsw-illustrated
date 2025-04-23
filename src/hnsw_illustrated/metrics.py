"""
© 2025, Stefan Webb. Some Rights Reserved.

Except where otherwise noted, this work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

"""

import numpy as np


def l2_distance(vector_one: np.array, vector_two: np.array):
    # TODO: Set axis?
    return np.linalg.norm(vector_two - vector_one, ord=2)
