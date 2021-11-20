# -*- coding: utf-8
from datetime import datetime as dt

def friday(day: str) -> str:
    int_day: int = dt.strptime(day, '%d.%m.%Y').weekday()
    result: int = (4 - int_day) % 7
    return result


if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
