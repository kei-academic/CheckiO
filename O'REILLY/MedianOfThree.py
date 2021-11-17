# -*- coding: utf-8

from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    ans = els[:2]
    for i in range(len(els)-2):
        arr = sorted([els[i], els[i+1], els[i+2]])
        ans.append(arr[1])
    return ans


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
