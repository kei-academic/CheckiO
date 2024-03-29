# -*- coding: utf-8 -*-

def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    words = ''
    for word in phrases:
        inclusion = word.find('right')
        if inclusion > -1:
            word = word.replace('right','left')
        words = words + word + ','
    return words[:-1]

    # another patttern
    return ','.join(word.replace('right', 'left') for word in phrases)


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
