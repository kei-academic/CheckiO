# -*- coding: utf-8 -*-

def checkio(values: list) -> list:
    abs_val = []
    for i in values:
        abs_val.append(abs(i))
        result = sorted(abs_val)
        for j in result:
            index = result.index(j)
            if j not in values:
                result[index] = -j
    return result

    # another pattern
    return sorted(values, key=abs)


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
