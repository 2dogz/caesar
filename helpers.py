def alpha_position(letter):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    return ord(letter) - start
def pos_to_char(pos):
    return chr(pos + 97)
def rotate_character(char, rot):
    if char.isalpha():
        b = (alpha_position(char) + rot) % 26 + 97
        return chr(b)
    else:
        return char
