# -*- coding: utf-8 -*-

def remove_brackets(line: str) -> str:
    def is_balanced(line: str) -> bool:
        if line == '':
            return True
        reduced_line = line.replace('[]','').replace('{}','').replace('()','')
        if reduced_line == line:
            return False
        return is_balanced(reduced_line)

    if is_balanced(line):
        return line
    result = ''
    for i in range(len(line)):
        tmp_res = remove_brackets(line[:i] + line[i+1:])
        if len(tmp_res) > len(result):
            result = tmp_res
    return result


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
