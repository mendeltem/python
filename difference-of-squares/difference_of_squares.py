def square_of_sum(count):
    c = 0
    for i in range(count+1):
        c += i
    return c**2

def sum_of_squares(count):
    c = 0
    for i in range(count+1):
        c += i**2
    return c

def difference(count):
    return square_of_sum(count)- sum_of_squares(count)



