# -*- coding: utf-8 -*-

from typing import List, Tuple
import math


def _is_intersected(circle1, circle2):
    dx = circle1[0] - circle2[0]
    dy = circle1[1] - circle2[1]
    d2 = dx ** 2 + dy ** 2
    d = math.sqrt(d2)
    min_r = min(circle1[2], circle2[2])
    max_r = max(circle1[2], circle2[2])

    # Disconnected.
    if min_r + max_r <= d:
        return False

    # Included.
    if d + min_r <= max_r:
        return False
    return True


def find_root(i, parents):
    if parents[i] is None:
        return i
    root = find_root(parents[i], parents)
    parents[i] = root
    return root


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    # Tree Structure.
    # The same group <=> the same root.
    parents = dict()
    for ci in range(len(circles)):
        intersections = [
            i for i in range(ci) if _is_intersected(circles[i], circles[ci])
        ]
        roots = set(find_root(i, parents) for i in intersections)
        for root in roots:
            parents[root] = ci
        parents[ci] = None

    result = len(set(find_root(i, parents) for i in range(len(circles))))
    return result


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
