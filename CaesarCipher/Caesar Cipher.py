# Made by Edgar Ray Tuyor
import string
print("Welcome to my Caesar Encryptor! ")
method= int(input('Enter 1 for Encyptor 2 for Decryptor: '))
password =str(input('Enter the Password to be Encrypted or Decrypted. :'))


def encryption():
    if method == 1:
        caesar_shift = int(input('Enter shift for caesar encryption: '))
        return caesaren(password,caesar_shift)
    elif method == 2: #Decryption
        alphabet = string.ascii_lowercase
        shift_key = int(input('Enter shift key: '))
        decrypted_message = ""
        for c in password:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - shift_key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c
        return decrypted_message

    else:
        print("invalid number. Will proceed to encryption")

def caesaren(text,s):
    res = ""
    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            res += chr((ord(char) + s-65) % 26 + 65)
        else:
            res += chr((ord(char) + s - 97) % 26 + 97)
    return res

print("Your new pass is " + encryption().join("''"))