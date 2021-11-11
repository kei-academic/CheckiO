# -*- coding: utf-8 -*-

def end_zeros(num: int) -> int:
    s = str(num)
    return len(s) - len(s.rstrip('0'))

    # another patterm
    return len(str(num)) - len(str(num).rstrip('0'))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
