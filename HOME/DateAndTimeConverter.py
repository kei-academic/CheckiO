# -*- coding: utf-8 -*-

def date_time(time: str) -> str:
    import datetime as dt
    d = dt.datetime.strptime(time, "%d.%m.%Y %H:%M")
    ans = d.strftime("%-d %B %Y year %-H hour %-M minute")
    if d.hour != 1:
        ans = ans.replace('hour', 'hours')
    if d.minute != 1:
        ans = ans.replace('minute', 'minutes')
    return ans

    # another pattern
    from datetime import datetime
    t = datetime.strptime(time, '%d.%m.%Y %H:%M')
    y, m, d, h, mi =  t.year, datetime.strftime(t, '%B'), t.day, t.hour, t.minute
    suffix = lambda n: 's' if n != 1 else ''
    return f'{d} {m} {y} year {h} hour{suffix(h)} {mi} minute{suffix(mi)}'


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
