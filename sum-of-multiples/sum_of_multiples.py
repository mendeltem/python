def sum_of_multiples(limit, multiples):
    return  sum({y for i in multiples for y in range(i, limit, i)})
