# -*- coding: utf-8 -*-

def middle(text):
    num: int = len(text)
    result: str = ""
    if num%2 == 0:
        result += text[num//2-1]
    result += text[num//2]
    return result


if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
