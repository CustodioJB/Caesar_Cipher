# Decrypting Text
def decrypt(encrypt_text, shift):
    decrypted_text = ''
    for i in range(len(encrypt_text)):
        if encrypt_text[i] == ' ':
            decrypted_text = decrypted_text + encrypt_text[i]
        elif encrypt_text[i].isupper():
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift-65)%26+65)
        else:
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift-97)%26+97)
    return decrypted_text

decrypted_text = decrypt("Wklv lv d whvw", 3)
print(decrypted_text)