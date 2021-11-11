# -*- coding: utf-8 -*-

def is_even(num: int) -> bool:
    num %= 2
    if num == 0:
        result = True
    else:
        result = False
    return result

    # another pattern
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
