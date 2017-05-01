import os, sys
import elementary

def File(filename):
    try:
        file = open(filename)
        text = file.readlines()
        print('--- '+filename)
        print(text)
    except FileNotFoundError:
        # HandleError()
        print(filename + ": No such file")

def main():
    args = sys.argv[1:]
    for arg in args:
        File(arg)

if __name__=='__main__':
    main()
