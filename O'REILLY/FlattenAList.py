# -*- coding: utf-8 -*-

from typing import List

def flat_list(array) -> List[int]:
    ans = []
    def get_flat(arr):
        for i in arr:
            if type(i) == int:
                ans.append(i)
            else:
                get_flat(i)
        return ans
    return get_flat(array)


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
