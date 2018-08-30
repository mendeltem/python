def sum_of_multiples(limit, multiples):
    list = []
    for i in range(limit):
        for z in multiples:
             if not (i % z) and i not in list:
                list.append(i)
    return sum(list)


