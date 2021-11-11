# -*- coding: utf-8 -*-

from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    result = [0, 0]
    for i in list(instructions):
        if i == 'f':
            result[1] += 1
        elif i == 'b':
            result[1] -= 1
        elif i == 'r':
            result[0] += 1
        else:
            result[0] -= 1
    return tuple(result)

    # another pattern
    f, b, l, r = (instructions.count(d) for d in 'fblr')
    return r-l, f-b


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
