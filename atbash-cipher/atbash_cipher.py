alpha = ["abcdefghijklnopqrstvwyz"]

def encode(plain_text):
    list_e = [u for i,y in enumerate(alpha)for u in y]
    list_d = sorted(list_e, reverse=True)

    text = [list_d[z] for i in plain_text for z,y in enumerate(list_e) if i == y ]
    encoded_text = ""
    for i in text:
        encoded_text += i
    return encoded_text


def decode(ciphered_text):
    list_e = [u for i,y in enumerate(alpha)for u in y]
    list_d = sorted(list_e, reverse=True)

    text = [list_d[z] for i in ciphered_text for z,y in enumerate(list_e) if i == y ]
    encoded_text = ""
    for i in text:
        encoded_text += i
    return encoded_text



#cipher_text = encode("abcdefg abcdefg")
#print(cipher_text)
#plain_text = decode(cipher_text)
#print(plain_text)