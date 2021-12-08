# -*- coding: utf-8 -*-

from typing import Dict

values: Dict[int, str] = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD',
                            100 : 'C', 90 : 'XC', 50 : 'L', 40: 'XL',
                            10 : 'X', 9 : 'IX', 5 : 'V', 4: 'IV', 1 : 'I'}

def checkio(data):
    ans = ""
    for n in sorted(values.keys(), reverse=True):
        while data >= n:
            ans += values[n]
            data -= n
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
