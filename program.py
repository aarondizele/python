# import os, math

# def fib(x):
#     x = 0
#     y = 1
#     while x < 255:
#         z = x + y
#         x = y
#         y = z
#     return z

# n = 5
# print fib(n)

# # def primeNumber(x):
# #     i = 0
# #     for i in 

# def h(x):
#     assert type(x) == int and x >= 0
#     answer = 0
#     s = str(x)
#     for c in s:
#         answer += int(c)
#     return answer

# print h(168)

def r1(x, L):
    
    t = len(L)
    for i in range(0, t):
        if x == L[i]:
            return True
    return False
        

x = 1
L = [1, 2, 3, 4, 5, 6, 7, 8]
print r1(x, L)