# -*- conding: utf-8 -*-

def is_majority(items: list) -> bool:
    t = f = 0
    for item in items:
        if item == True:
            t += 1
        else:
            f += 1
    if t > f:
        ans = True
    else:
        ans = False
    return ans


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
