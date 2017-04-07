import os
import sys
import math

# def isPrime(n):
# 	isPrime = True
# 	i = 2
# 	for x in range(i <= math.sqrt(n)):
# 		if(n % i == 0):
# 			isPrime = False
# 			break
# 	if(isPrime):
# 		print(n, " is a prime number")
# 	else:
# 		print(n, " is not a prime number")

# z = 7
# print(isPrime(z))

def allFactorInList(n):
	A = {}
	i = 1
	for x in range(i <= math.sqrt(n)):
		if(n % i == 0 ):
			A[i] = x
			if( i != math.sqrt(n)):
				A[i] = n/x
		print(A[i], " ")

n = 36
allFactorInList(n)



# print(sys.getsizeof('a'))
# print(sys.getsizeof('A'))


# def Factorial(x):
#     global numCalls
#     numCalls += 1
#     print("I'm computing ", x)
#     if x == 0: return 1
#     n = Factorial(x - 1) * x
#     print("Done!", x, " = ", n)
#     return n

# z = 3
# numCalls = 0
# print(Factorial(z))
# print('numCalls =', numCalls)

# def fib(n):
# 	global numCalls
# 	numCalls += 1
# 	# print 'fib called with', n
# 	if n <= 1:
# 		return n
# 	else:
# 		return fib(n-1) + fib(n-2)

# numCalls = 0
# n = 3
# print('fib of', n, ' = ', fib(n))
# print('numCalls =', numCalls)

# def Fib(n):
#     global numCalls
#     numCalls += 1
#     print("Fib called with ", n)
#     if(n <= 1): 
#         return n
#     else:
#         return Fib(n-1) + Fib(n-2)

# z = 6
# numCalls = 0
# print('fib of', z, ' = ', Fib(z))
# print('numCalls =', numCalls)
