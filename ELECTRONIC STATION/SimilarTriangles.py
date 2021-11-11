# -*- coding: utf-8 -*-

from typing import List, Tuple
Coords = List[Tuple[int, int]]
Coord = Tuple[int, int]

def square_lengths(a: Coord, b: Coord, c: Coord) -> List[int]:
    l1 = (b[0] - a[0])**2 + (b[1] - a[1])**2
    l2 = (c[0] - b[0])**2 + (c[1] - b[1])**2
    l3 = (a[0] - c[0])**2 + (a[1] - c[1])**2
    return sorted([l1, l2, l3])

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    sides1 = square_lengths(coords_1[0], coords_1[1], coords_1[2])
    sides2 = square_lengths(coords_2[0], coords_2[1], coords_2[2])
    ans: bool = sides1[0]/sides2[0] == sides1[1]/sides2[1] and sides1[0]/sides2[0] == sides1[2]/sides2[2]
    return ans


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
