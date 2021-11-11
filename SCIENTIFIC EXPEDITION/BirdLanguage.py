# -*- coding: utf-8 -*-

def translate(text: str) -> str:
    vowel: list = ["a", "e", "i", "o", "u", "y"]
    result: str = ""
    c: int = 0
    while c < len(text):
        result += text[c]
        if text[c] in vowel:
            c += 3
        elif text[c] == ' ':
            c += 1
        else:
            c += 2
    return result


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
