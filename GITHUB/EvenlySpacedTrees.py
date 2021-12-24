# -*- coding: utf-8 -*-
from typing import List
from math import gcd

def evenly_spaced_trees(trees: List[int]) -> int:
    if len(trees) < 3:
        return 0
    diff_trees = [x - trees[0] for x in trees]
    diff = 100
    for i in range(1, len(diff_trees)-1):
        diff = min(gcd(diff_trees[i], diff_trees[i+1]), diff)
    ans = 0
    for i in range(trees[0], trees[-1], diff):
        if i not in trees:
            ans += 1
    return ans


if __name__ == '__main__':
    print("Example:")
    print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    print("Coding complete? Click 'Check' to earn cool rewards!")
