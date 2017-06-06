from helpers import alphabet_position, rotate_character

def encrypt(text, key):  
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = alphabet.upper()
    textUpper = text.upper()
    accumulator = ''
    x = 0
    for i in text:
        
        
        iUpper = i.upper()
        if alphabetUpper.count(iUpper) < 1:
            accumulator = accumulator + i
            
        else:
            
            
            
           
            spotAccumulator = x % ((len(key)))
            rotationChar = key[spotAccumulator]
            rotation = alphabet_position(rotationChar.upper())
            finalChar = rotate_character(i, rotation)
            x = x + 1
            accumulator = accumulator + finalChar
            
            

                
    return accumulator


def main():
    userInput = input("Type a message:")
    userRotation = input("Encryption key:")
    print(encrypt(userInput, userRotation))
    # your main code (input and print statements)

if __name__ == "__main__":
    main()


























