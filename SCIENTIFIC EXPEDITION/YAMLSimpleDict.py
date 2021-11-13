# -*- coding: utf-8 -*-

def yaml(text):
    def transform(value):
        keywords = {'': None, 'null': None, 'true': True, 'false': False}
        try:
            return int(value)
        except ValueError:
            if value in keywords:
                return keywords[value]
            if value.startswith('"') and value.endswith('"'):
                return value[1:-1].replace(r'\"', '"')
            return value

    result = {key: transform(value) for key, _, value in (map(str.strip, line.partition(':'))
            for line in text.splitlines()) if key}
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
    'class': '12b',
    'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
