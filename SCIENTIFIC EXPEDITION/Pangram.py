# -*- coding: utf-8 -*-

def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    count: int = 0
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in text.lower():
            count += 1
    return count == 26

    # another pattern
    return len({i for i in text.lower() if 'a' <= i <= 'z'}) == 26


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
