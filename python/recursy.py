# def rec(x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)

# rec(1)

# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
# print(fact(4))

# def fibonacci(x):
#     if x == 1:
#         return 0
#     if x == 2:
#         return 1
#     return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(4))

# def pal(str):
#     if len(str) <= 1:
#         return True
#     if str[0] != str[-1]:
#         return False
#     return pal(str[1:-1])

# print(pal('labal'))
# print(pal('labad'))
# print(pal(''))
# print(pal('a'))

# def str_modify(str):
#      if len(str) == 1 or len(str) == 2:
#           return str
#      return str[0]+'('+ str_modify(str[1:-1])  +')'+str[-1]

# print(str_modify('Katya'))
# print(str_modify('Katy'))
# print(str_modify('Ka'))

# def str_modify(s):
#      if len(s) == 0 or len(s) == 1:
#           return s
#      if len(s) == 2:
#           return s[0] + '*' + s[1]
#      return s[0] + '*' + str_modify(s[1:-1])  + '*' + s[-1]

# print(str_modify('Katya'))
# print(str_modify('K'))
# print(str_modify('KatyaKatyaKatyaKatya'))

# def str_modify(s):
#      if len(s) == 0:
#           return s
#      if s[0] == '(':
#           return s[0] + str_modify(s[1:]) + ')'
#      return s[0] + str_modify(s[1:]) + s[0]

# print(str_modify('(jhu((uf(((hjhifd(b'))

# возведение в степень
# def power(x,n):
#      if n == 1:
#           return x
#      return x*power(x, n-1)

# print(power(2,2))
# print(power(2,3))
# print(power(3,2))
# print(power(2,4))

# def sum_nums(num):
#      num = str(num)
#      if len(num) == 1:
#           return int(num)
#      return int(num[0]) + sum_nums(num[1:])
     
# print(sum_nums(23134))
# print(sum_nums(5))
# print(sum_nums(27))
# print(sum_nums(10))

# a = [1, 2, [2, 3, 4, [2, 3], 5]]

# def rec(s, l = 1):
#      print(*s, 'level=', l)
#      for i in s:
#           if type(i) == list:
#                rec(i, l+1)
# rec(a)