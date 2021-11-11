# -*- coding: utf-8 -*-

def checkio(line1: str, line2: str) -> str:
    s_line1 = set(line1.lower().split(','))
    s_line2 = set(line2.lower().split(','))
    result = ','.join(sorted(s_line1 & s_line2))
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
        'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
