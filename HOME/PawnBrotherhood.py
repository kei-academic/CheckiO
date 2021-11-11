# -*- coding: utf-8 -*-

def safe_pawns(pawns: set) -> int:
    result = 0
    for pawn in pawns:
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns:
            result += 1
        elif chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns:
            result += 1
    return result

    #another pattern
    p = {(ord("8")-ord(x[1]), ord(x[0])-ord("a")) for x in pawns}
    s1 = {(x[0]-1,x[1]-1) for x in p}
    s2 = {(x[0]-1,x[1]+1) for x in p}
    return len(p & s1 | p & s2)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
