# -*- coding: utf-8 -*-

from typing import List

def letter_queue(commands: List[str]) -> str:
    result: str = ''
    for i in commands:
        if i == 'POP':
            result = result[1:]
        else:
            word = i[-1]
            result += word
    return result

    # another pattern
    from collections import deque
    total = deque('')
    for s in commands:
        if s == 'POP':
            if total:
                total.popleft()
        else:
            total.append(s[-1])
    return ''.join(total)


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
