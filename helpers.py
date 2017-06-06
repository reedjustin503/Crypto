def alphabet_position(letter):
    bigletter = letter.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    return alphabet.index(bigletter)


def rotate_character(char, rot):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerAlphabet = alphabet.lower()
    
    if alphabet.count(char.upper()) < 1:
        return char
    else:
        numChar = alphabet_position(char)
        rotatedCharNumber = (numChar + rot) % 26
        if char == char.upper():
            newChar = alphabet[rotatedCharNumber]
            return newChar
        else:
            lowerNewChar = lowerAlphabet[rotatedCharNumber]
            return lowerNewChar
