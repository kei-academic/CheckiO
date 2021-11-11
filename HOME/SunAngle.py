# -*- coding: utf-8 -*-

from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    hours, minutes = map(int, time.split(':'))
    angle = 15 * hours + minutes / 4 - 90
    if 0 <= angle <= 180:
        return angle
    else:
        return "I don't see the sun!"

    # another pattern
    t = int(time[:2]) * 15 + int(time[3:]) / 4 - 90
    return t if 0 <= t <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
