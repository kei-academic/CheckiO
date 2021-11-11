# -*- coding: utf-8 -*-

def checkio(words: str) -> bool:
    count = 0
    word_list = list(words.split())
    for word in word_list:
        count = (count + 1) * word.isalpha()
        if count == 3:
            return True
    else:
        return False

    # another pattern
    import re
    return bool(re.search('\D+ \D+ \D+', words))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
