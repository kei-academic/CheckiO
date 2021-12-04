# -*- coding: utf-8 -*-

def checkio(number: int) -> int:
    fed = minute = pigeons = 0
    while number >= 0:
        number -= pigeons
        minute += 1
        if number <= 0:
            return fed
        if minute < number:
            fed += minute
            number -= minute
        else:
            fed += number
            return fed
        pigeons += minute
    return fed


if __name__ == '__main__':
    print("Example:")
    print(checkio(1))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
