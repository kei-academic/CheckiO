# -*- coding: utf-8 -*-

def checkio(text: str) -> str:
    text: str = text.lower()
    l_text = []
    for i in range(ord('a'), ord('z') + 1):
        index = [chr(i), text.count(chr(i))]
        l_text.append(index)
    l_text.sort(key=lambda x: (-x[1], x[0]))
    result = l_text[0][0]
    return result

    # another pattern
    import string
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
