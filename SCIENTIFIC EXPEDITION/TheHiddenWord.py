# -*- coding: utf-8 -*-

import itertools as it

def checkio(text, word):
    horizontal = text.lower().replace(' ', '').split('\n')
    for i, row in enumerate(horizontal, 1):
        index = row.find(word)
        if index >= 0:
            return [i, index+1, i, index+len(word)]
    vertical = [''.join(line) for line in it.zip_longest(*horizontal, fillvalue=' ')]
    for i, col in enumerate(vertical, 1):
        index = col.find(word)
        if index >= 0:
            return [index+1, i, index+len(word), i]

    #another pattern
    def find_word_in_multiline(lines):
        for row, line in enumerate(lines):
            col = line.find(word)
            if col != -1:
                return True, row + 1, col + 1
        else:
            return False, 0, 0
    cut = [line.lower().replace(' ', '') for line in text.splitlines()]
    found, y, x = find_word_in_multiline(cut)
    if found:
        return [y, x, y, x + len(word) - 1]
    else:
        transposed_cut = [''.join(chars) for chars in it.zip_longest(*cut, fillvalue=' ')]
        found, x, y = find_word_in_multiline(transposed_cut)
        return [y, x, y + len(word) - 1, x]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
        And dreaming often, dear,
        I dreamed that, if I counted all,
        -How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
        Long time the manxome foe he sought--
        So rested he by the Tumtum tree,
        And stood awhile in thought.
        And as in uffish thought he stood,
        The Jabberwock, with eyes of flame,
        Came whiffling through the tulgey wood,
        And burbled as it came!""", "noir") == [4, 16, 7, 16]
    print("Coding complete? Click 'Check' to earn cool rewards!")
