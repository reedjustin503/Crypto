from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    rotatedText = ''
    for i in text:
        rotatedChar = rotate_character(i, rot)
        rotatedText = rotatedText + rotatedChar
    return rotatedText

def main():
    userInput = input("Type a message:")
    userRotation = int(input("Rotate by:"))
    print(encrypt(userInput, userRotation))
    # your main code (input and print statements)

if __name__ == "__main__":
    main()