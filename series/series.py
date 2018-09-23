def slices(series, length):
    solution = []
    length_of_series = len(series)
    if series == "" or length <= 0 or length > length_of_series:
        raise ValueError("Error")
    temp= ""
    for s,i in enumerate(series):

        if length_of_series < length:
            break
        for z,x in enumerate(series):
            if z < length:
                temp += series[z+s]
            if z == length-1:
                solution.append(temp)
                temp = ""
        length_of_series -= 1
    return solution
