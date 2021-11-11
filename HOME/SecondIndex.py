# -*- coding: utf-8 -*-

from typing import Union

def second_index(text: str, symbol: str) -> Union[int, None]:
    """
        returns the second index of a symbol in a given text
    """
    div = list(text)
    if symbol in div:
        del div[text.find(symbol)]
    if symbol in div:
        result = ''.join(div).find(symbol) + 1
    else:
        result = None
    return result

    # another pattern
    if text.count(symbol) > 1:
        return text.index(symbol,text.index(symbol) + 1)
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
