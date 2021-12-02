# -*- coding: utf-8 -*-

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if len(line) == 0:
        return 0
    if len(set(list(line))) == 1:
        return len(line)
    ans = 1
    count = 1
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            count += 1
        else:
            if count > ans:
                ans = count
            count = 1
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
