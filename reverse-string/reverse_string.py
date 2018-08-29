def reverse(text):
    t_o = ""; i = -1
    for t in range(len(text)):
        t_o += text[i]
        i -= 1
    return t_o
