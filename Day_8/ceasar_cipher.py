import caesar_cipher_art

print(caesar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defining the cipher/decypher function
def caesar(direction, text, shift):
    result = ""
    encrypted_decrypted = ""
    for letter in text:
        if letter in alphabet:
            #Encrypting
            if direction == "encode":
                index = alphabet.index(letter) + shift
                encrypted_decrypted = "encrypted"
            #Decrypting
            else:
                index = alphabet.index(letter) - shift
                encrypted_decrypted == "decrypted"
            index = index % len(alphabet)
            # We use modulo to deal with lengths> 25. If <25, it will return the same number, if > it will return the exact position after 25, no matter the times it fits into it.
            result += alphabet[index]
            #If the input string contains symbols or numbers, the else statement will add them to the result.
        else:
            result += letter
    print(f"This is your {encrypted_decrypted} message: {result}.\n")

#Adding a continue_cipher variable to use in the loop as True or False to exit the while loop
continue_cipher = True

#Using a while loop to continue encoding/decoding
while continue_cipher:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
    #Checking correct encode/decode input
    if direction != "encode" and direction != "decode":
        print("Wrong input.")
        continue
    text = input('Type your message:\n').lower()
    #Checking the shift input is a number
    shift =  0
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Not a number!")
        continue

    caesar(direction, text, shift)

    restart = input('Type "yes" to encrypt/decrypt another message, type "no" to exit.\n').lower()
    if restart == "no":
        continue_cipher = False


