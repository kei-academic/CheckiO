# -*- coding: utf-8 -*-

MORSE = {
    ".-": "a", "-...": "b", "-.-.": "c",
    "-..": "d", ".": "e", "..-.": "f",
    "--.": "g", "....": "h", "..": "i",
    ".---": "j", "-.-": "k", ".-..": "l",
    "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r",
    "...": "s", "-": "t", "..-": "u",
    "...-": "v", ".--": "w", "-..-": "x",
    "-.--": "y", "--..": "z",
    "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5",
    "-....": "6", "--...": "7", "---..": "8",
    "----.": "9",
    "s":" "
}


def morse_decoder(code):
    word = []
    for i in code.split("   "):
        org = ""
        char = i.split(" ")
        for morse in char:
            org += MORSE.get(morse, str(morse))
        word.append(org)
    result = " ".join(word).capitalize()
    return result

    # another pattern
    return ''.join(MORSE[char] for char in code.replace('   ', ' s ').split()).capitalize()


if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- ..."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert (
        morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
        == "It was a good day"
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
