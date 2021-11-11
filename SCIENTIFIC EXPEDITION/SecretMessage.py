# -*- coding: utf-8 -*-

def find_message(message: str) -> str:
    result: str = ""
    for i in list(message):
        if i.isupper():
            result += i
    return result

    # another pattern
    return ''.join(i for i in message if i.isupper())


if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
        + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
        + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
