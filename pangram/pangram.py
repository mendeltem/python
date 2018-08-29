def is_pangram(sentence):
    e = [];z = 0
    for i in sentence.lower():
        if chr(96) < i  < chr(123) and i not in e:
            e.append(i)
            z +=1
    if(z >= 26):
        return True
    return False

