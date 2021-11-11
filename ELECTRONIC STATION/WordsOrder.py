# -*- coding: utf-8 -*-

def words_order(text: str, words: list) -> bool:
    text: list[str] = text.split()
    result: bool = True
    for word in words:
        if word not in text:
            result = False
            break
        for i in range(len(words)-1):
            if text.index(words[i]) > text.index(words[i+1]):
                result = False
                break
            if words[i] == words[i+1]:
                result = False
                break
    return result


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'im', 'here']) == True
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
