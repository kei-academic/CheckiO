# -*- coding: utf-8 -*-

def split_list(items: list) -> list:
    import math as m
    harf = m.ceil(len(items)/2)
    return [items[:harf], items[harf:]]

    #another pattern
    mid = (len(items) + 1) // 2
    return [items[:mid], items[mid:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
