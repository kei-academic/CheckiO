# -*- coding: utf-8 -*-

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    length = len(data)
    sort_data = []
    for i in range(length):
        for j in range(i, length):
            if data[j]['price'] > data[i]['price']:
                high = data[i]
                data[i] = data[j]
                data[j] = high
    for i in range(limit):
        sort_data.append(data[i])
    return sort_data

    # another pattern
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
