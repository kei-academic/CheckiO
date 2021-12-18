# -*- coding: utf-8 -*-
from typing import Set, List, Tuple

def create_intervals(data: Set[int]) -> List[Tuple[int]]:
    """
        Create a list of intervals out of set of ints.
    """
    if not data:
        return []
    data = sorted(data)
    ans = []
    start = last = data[0]
    for i in data[1:]:
        if (i - last) > 1:
            ans.append((start, last))
            start = i
        last = i
    if start:
        ans.append((start, last))
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
