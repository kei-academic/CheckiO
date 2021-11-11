# -*- coding: utf-8 -*-

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    text = text.split(begin)
    text = text[1]
    text = text.split(end)
    return text[0]

    # another pattern
    return text[text.find(begin) + 1:text.find(end)]
    return text[text.index(begin) + 1:text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
