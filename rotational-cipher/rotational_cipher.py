def rotate(text, key):
    string= ""
    for i in text:
        if 48 < ord(i) < 57 or ord(" ") == ord(i) or ord(i) == ord("!") or ord(i)== ord("'") or ord(i)== ord(",") or ord(i)== ord(".") :
            z = ord(i)
        else:
            z = ord(i) + key
        if  90 < z  and  i.isupper()  or 122 < z and i.islower():
            z -= 26
        if i == " " or i=="<" or i==">":
            string += " "
        else:
            string += chr(z)
    return string


