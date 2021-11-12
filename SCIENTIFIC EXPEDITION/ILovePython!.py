# -*- coding: utf-8 -*-

def i_love_python():
    """
        Python is the language I use most often.
        I have the impression that it is often used for machine learning.
    """
    ans = "I love Python!"
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
