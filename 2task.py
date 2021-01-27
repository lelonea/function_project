def fact(n):
    ind = 0
    res = 1
    while ind < n:
        ind +=1
        res *= ind
    print(res)
    return res
fact(5)
