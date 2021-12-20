# -*- coding: utf-8 -*-

def repeat_inside(line: str) -> str:
    """
        first the longest repeating substring
    """
    ans = ''
    for i in range(len(line)):
        for j in range(len(line) - i):
            s = line[i:i + j + 1]
            for repeat in range(2, len(line) // len(s) + 1):
                ls = s * repeat
                if (ls in line) and (len(ls) > len(ans)):
                    ans = ls
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
