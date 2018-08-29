def verify(isbn):
    list = []
    z = 1
    lenx = len(isbn)
    for i in isbn:
        if z >= lenx and i =="X":
                list.append(10)
        elif i != "-" and not i.isnumeric():
            return False
        elif i.isnumeric():
            list.append(i)
        z += 1
    if len(list) != 10:
        return False
    temp = 0
    k = 10
    for z in list:
        temp = temp + int(z) * k
        k -= 1
    if temp % 11 == 0:
        return True
    return False

