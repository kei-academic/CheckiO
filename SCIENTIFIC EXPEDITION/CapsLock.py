# -*- coding: utf-8 -*-

def caps_lock(text: str) -> str:
    l_text: list = list(text)
    result: str = l_text[0]
    turn_a: bool = False
    for i in l_text[1:]:
        if i == 'a':
            turn_a = not turn_a
        else:
            if turn_a:
                result += i.upper() if i.islower() else i.lower()
            else:
                result += i
    return result

    # another pattern
    not_a: bool = True
    result: str = ""
    for i in text:
        if i == 'a':
            not_a = not not_a
        if not_a:
            result += i
        else:
            if i.islower():
                result += i.upper()
            else:
                result += i.lower()
        result = result.replace('a', '').replace('A', '')
        if text[0] == 'A':
            result = 'A' + result
    return result


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
