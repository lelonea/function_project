# a = ['buba', 'nani', 'huba']
# b = [i[::-1] for i in a]
# print(b)

# a = ['mike', 'ben', 'alex', 'misha']
# b = [i for i in a if 'a' in i]
# print(b)

# a = [{'sn': 18298198, 'gv': 1998}, {'sn': 73618763, 'gv': 2005}, {'sn': 84248297, 'gv': 2003}]
# b = [i for i in a if i['gv'] > 2000]
# print(b)


# from random import randint
# n = 3
# m = [[randint(1,9) for j in range(n)] for i in range(n)]
# print(m)
# print(randint(1,9))


# a = {'aa': 1, 'b': 2, 'cccc': 4}
# b = {v: str(k) for k, v in a.items()}
# print(b)


# def main():
#     print('bah')
#     return
#
# if __name__ == '__main__':
#     main()


#/////////////
# a = [1, 4, 3, 1, 4, 2, 5, 6, 2, 7]
# b = set(a)
# c = {}
# # def test(a, b):
# for i in a:
#     c[i] = 0
#     v = 1
#     if i in b:
#         v += 1
#     c[i] = v
# print(c)
# ////////////

# func = lambda x = input('name:  '): 'Hello ' + x
#
# print(func())

# b = []
# while True:
#     a = input('name: ')
#     if a == '0':
#         break
#     b.append(a)
#
# # for i in b:
# #     func = lambda i: ['Hello, ' + i]
# #     print(func(i))
#
# func = lambda b: [f'hello {i}' for i in b]
# print(func(b))


# a = map(lambda x: x **2, [1,2,3,4,5,6])
# print(list(a))

# a = [1, 3, 4, 6, 2, 4, 7]
# # b = map (lambda x: str(x), a)
# # print(list(b))


# a = [1, 3, 4, 6, 2, 4, 7]
# b = filter(lambda x: x % 2 == 0, a)
# print(list(b))

# a = ['kira', 'mike', 'mary']
# b = filter(lambda x: 'k' in x, a)
# print(list(b))


from functools import reduce

items = [1, 2, 3, 4, 5, 6]
summ = reduce(lambda x, y: x * y, list(filter(lambda x: x % 3 == 0, items)))
print(summ)
