def encrypt(text, rot):
    # receives as input a string and an integer.
    # return the result of rotating each letter in the text by rot places to the right.
    new_mess = ''
    for char in text:
        new_char = rotate_character(char, rot)
        new_mess += new_char

    return new_mess

def alphabet_position(letter):
    # receives a letter and returns the position of that letter in the alphabet
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numeral = alphabet.find(letter)

    return numeral


def rotate_character(char, rot):
    # return a new string of length 1, the result of rotating char by rot number
    # of places to the right.

    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_pos = (alphabet_position(char) + (rot % len(alphabet)) - 26)

    if char in alpha_upper or char in alphabet:
        if char.isupper() == True:
            new_letter = alpha_upper[new_pos]
        else:
            new_letter = alphabet[new_pos]
        return new_letter

    else:
        return char
