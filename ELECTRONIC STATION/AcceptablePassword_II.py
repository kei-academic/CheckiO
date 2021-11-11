# -*- codig: utf-8 -*-

def is_acceptable_password(password: str) -> bool:
    result: bool = False
    if len(password) >= 6:
        for i in password:
            if i.isdigit():
                result = True
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
