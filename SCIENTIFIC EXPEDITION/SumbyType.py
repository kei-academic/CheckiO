# -*- coding: utf-8 -*-

from typing import Tuple

def sum_by_types(items: list) -> Tuple[str, int]:
    strings: str = ""
    integers: int = 0
    for i in items:
        try:
            strings += i
        except TypeError:
            integers += i
    return (strings, integers)

    # another pattern
    return (''.join(x for x in items if isinstance(x, str)), sum(x for x in items if isinstance(x, int)))


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
