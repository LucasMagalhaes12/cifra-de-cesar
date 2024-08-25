import string

def encrypt(text, step):
    textEncrypted = ""
    for letter in text:
        if letter not in string.ascii_letters:
            textEncrypted += letter
        elif letter.islower():
            textEncrypted += chr(((ord(letter)-97+step)%26)+97)
        elif letter.isupper():
            textEncrypted += chr(((ord(letter)-65+step)%26)+65)
    return textEncrypted


def decrypt(text, step):
    textDecrypted = ""
    for letter in text:
        if letter not in string.ascii_letters:
            textDecrypted+= letter
        elif letter.islower():
            textDecrypted+= chr(ord(letter)+26-step) if ord(letter)-step<97 else chr(ord(letter)-step)
        elif letter.isupper():
            textDecrypted+= chr(ord(letter)+26-step) if ord(letter)-step<65 else chr(ord(letter)-step)
    return textDecrypted