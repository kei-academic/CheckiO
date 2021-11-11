# -*- coding: utf-8 -*-

import unicodedata as ud

def checkio(in_string):
    string = ud.normalize('NFKD', in_string).encode('ascii','ignore').decode('ascii','ignore')
    if string != "":
        result = string
    else:
        result = in_string
    return result

    # another pattern
    return ''.join(i for i in ud.normalize('NFD', in_string) if not ud.combining(i))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
