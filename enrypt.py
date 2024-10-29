import random
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encrypt
def encrypt_():    
    plain_text = input("Gib eine Nachricht ein Die du verschlüsseln möchtest: ")
    crypt_text = ""
    
    for letter in plain_text:
        index = chars.index(letter)
        crypt_text += key[index]
    
    print(f"Originaler Text: {plain_text}")
    print(f"Verschlüsselter Text: {crypt_text}")
    choice_()

#Decrypt 
def decrypt_():    
    crypt_text = input("Gib eine Nachricht ein Die du entschlüsseln möchtest: ")
    plain_text = ""
    
    for letter in crypt_text:
        index = key.index(letter)
        plain_text += chars[index]
    
    print(f"Originaler Text: {crypt_text}")
    print(f"Verschlüsselter Text: {plain_text}")
    
    choice_() 
def choice_():
    choice = input("Möchtest du eine Nachricht ver- oder entschlüsseln ? (V/E)").lower()
    if choice == "v":
        encrypt_()
    
    elif choice == "e":
        decrypt_()
    
    else:
        print("Falsche Angabe ! V oder E !")
        choice_()

choice_()
