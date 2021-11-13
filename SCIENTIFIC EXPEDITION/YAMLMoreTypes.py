# -*- coding: utf-8 -*-

from typing import Dict

BOOLS = ['false', 'true']

def yaml(a) -> Dict:
    ans = {}
    for line in a.splitlines():
        split_index = line.find(':')
        if split_index != -1:
            name, val_str = line[:split_index].strip(), line[split_index + 1:].strip()
            if val_str.startswith('"') and val_str.endswith('"'):
                value = val_str[1:-1].replace('\\"', '"')
            elif val_str in BOOLS:
                value = bool(BOOLS.index(val_str))
            elif val_str.isdigit():
                value = int(val_str)
            elif val_str == 'null' or not val_str:
                value = None
            else:
                value = val_str
            ans[name] = value
    return ans


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
        'age: 12\n'
        '\n'
        'class: 12b') == {'age': 12,
            'class': '12b',
            'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
        'age: 12\n'
        '\n'
        'class: 12b') == {'age': 12,
            'class': '12b',
            'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
        'age: 12\n'
        '\n'
        'class: 12b') == {'age': 12,
            'class': '12b',
            'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
        'children: 6\n'
        'alive: false') == {'alive': False,
            'children': 6,
            'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
        'children: 6\n'
        'coding:') == {'children': 6,
            'coding': None,
            'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
        'children: 6\n'
        'coding: null') == {'children': 6,
            'coding': None,
            'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
        'children: 6\n'
        'coding: "null" ') == {'children': 6,
            'coding': 'null',
            'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
