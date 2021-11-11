# -*- coding: utf-8 -*-

def goes_after(word: str, first: str, second: str) -> bool:
    if first in word and second in word:
        if word.index(second) - word.index(first) == 1:
            result = True
        else:
            result = False
    else:
        result = False
    return result

    # another pattern
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
