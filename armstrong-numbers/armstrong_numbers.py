def is_armstrong(number):
    zahl = 0
    for i in str(number):
        zahl+= (int(i) ** len(str(number)))
    if number == zahl:
        return True
    return False

print(is_armstrong(10))