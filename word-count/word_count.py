def word_count(phrase):
    word = ""
    dictionary = {}
    phrase += " "
    for i in phrase.lower():
        if  chr(96) < i < chr(123) or i == chr(39) or chr(47) < i < chr(58):
            word += i
        elif word != "":
            word =word.strip("'")
            if word not in dictionary:
                dictionary[word] =1
            else:
                dictionary[word] +=1
            word = ""
    return dictionary

