'''
Argparse is a module that allows for neat and familiar option and argument passing for our python programs. Help functions, and useful for handling a command line
'''


import os
import sys
from argparse import ArgumentParser

# def fibFast(n, memo):
#     if not n in memo:
#         memo[n] = fibFast(n-1, memo) + fibFast(n-2, memo)
#     return memo[n]
def fib(n):
    a,b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
# def fib(n):
#     memo = {0:1, 1:1}
#     return fibFast(n, memo)

def Main():

    # parser = argparse.ArgumentParser()
    parser = ArgumentParser()

    '''
    ### add group options
    '''
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("num", help="The fibonacci number tou wish to calculate or compute.", type=int)
    parser.add_argument("-o", "--output", help="Output result to a file", action="store_true")

    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The "+str(args.num)+"th fib number is : "+str(result))
    elif args.quiet:
        print(result)
    else:
        print("Fib("+str(args.num)+") = "+str(result))

    if args.output:
        f = open("fibonacci.txt", "a") ### 'w+': overwritten all file, 'r+': read a file, 'a': append data in file without crash previous data 
        f.write("The Fibonacci suite of "+str(args.num)+" : "+str (result)+'\n')
        f.close()





if __name__=='__main__':
    Main()