'''
In this kata you are required to, given a string,
replace every letter with its position in the alphabet.

If anything in the text isn't a letter,
ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
'''

# Example 1
def alphabet_position(text):
    alphabet_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }

    position_list = []

    for char in text.lower():
        if char in alphabet_dict:
            position_list.append(str(alphabet_dict[char]))

    return ' '.join(position_list)


# Best and shortest example:
def alphabet_position_2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


if __name__ == '__main__':
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown fox jumps over the lazy dog."

    output1 = alphabet_position(text1)
    output2 = alphabet_position_2(text2)

    print(output1)
    print(output2)

