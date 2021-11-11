# -*- coding: utf-8 -*-

def from_camel_case(name: str) -> str:
    camel_name: str = name[0].lower()
    for i in name[1:]:
        if 'A' <= i <= 'Z':
            camel_name += '_' + i.lower()
        else:
            camel_name += i
    return camel_name


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
