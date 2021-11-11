# -*- coding: utf-8 -*-

def time_converter(time):
    format24, m = map(int, time.split(":"))
    hour: int = format24 % 12 or 12
    if format24 < 12:
        ampm: int = 'a.m.'
    else:
        ampm: int = 'p.m.'
    format12 = f"{hour}:{m:02d} {ampm}"
    return format12

    # another pattern
    format24, m = map(int, time.split(':'))
    if format24 > 12:
        h = format24 - 12
        ampm = 'p.m.'
    else:
        h = format24
        ampm = 'a.m.' if h != 12 else 'p.m.'
    format12 = '%d:%02d %s' % (h, m, ampm)
    return format12


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
