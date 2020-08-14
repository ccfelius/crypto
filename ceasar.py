
def ceasar_cipher(text, key, decrypt = True):

    """
    Ceasar cipher method for decryption
    :param text: String
    :param key:  Integer 1-26
    :param decrypt: True, False
    :return: Decrypted message
    """

    text_ = list(text.lower())
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    message = []

    if decrypt == True:
        for i in text_:
            if i in alphabet:
                index = alphabet.index(i)
                newindex = (index - key) % 26
                new_char = alphabet[newindex]
                message.append(new_char)
            else:
                message.append(i)
    else:
        for i in text_:
            if i in alphabet:
                index = alphabet.index(i)
                newindex = (index + key) % 26
                new_char = alphabet[newindex]
                message.append(new_char)
            else:
                message.append(i)


    return "".join(message)


# Test case

d = "BMFY NX FKKQZJSHJ? IJHWJFXNSL DTZW BNXMJX, FSI GJNSL XFYNXKNJIBNYM BMFY NX JSTZLM KTW DTZ."
e = "what is affluence? decreasing your wishes, and being satisfiedwith what is enough for you."

print(ceasar_cipher(d, 5))
print(ceasar_cipher(e, 5, False))