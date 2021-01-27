# def fact(n):
#     ind = 0
#     res = 1
#     while ind < n:
#         ind +=1
#         res *= ind
#     print(res)
#     return res
# fact(5)
#
# def form(string, char='!'):
#     res_string = f'{char} {string} {char}'
#
#     return res_string
#
#
# print(form('nast'))

def pl(*args):
    b = args
    ind = 0
    res = 0
    for i in b:
        res += b[ind] * b[-1]
        ind += 1
    print(res)
    print(b)
    return b

pl(1, 2, 5)

