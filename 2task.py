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

# def pl(*args):
#     b = args
#     ind = 0
#     res = 0
#     for i in b:
#         res += b[ind] * b[-1]
#         ind += 1
#     print(res)
#     print(b)
#     return b
#
# pl(1, 2, 5)

# def func(a, b):
#     summ = a + b
#     digg = a - b
#     return summ, digg
# summr, diggr = func(3, 4)
# print(summr)

# def func(*args):
#     res = 0
#     ind = 0
#     b = args
#     max = 0
#     for i in b:
#         res += b[ind]
#         ind += 1
#         if i > b[-1] and i > max:
#             max = i
#     print(max)
#     print(res)
#
# func(1, 4, 3, 5, 8)
# not working!!!


# def func(**kwargs):
#     for k, w in kwargs.items():
#         print(k, w)
#         print(kwargs)
#
# func(a=5)

def dict(*args, **kwargs):
    print(args)
    print(kwargs)
dict( a = 5, c = 5)
