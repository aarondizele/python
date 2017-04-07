import sys

# d = {'a': 'Maman', 'b': 'Papa', 'c':'Grand Father', 'd': 'Grand Mother', 'e': 'Son', 'f': 'Daughter'}

# for k in sorted(d.keys()): 
#     print('Key '+k.upper()+' -> '+d[k])
# print(d.items()[0])

def File(filename):
    f = open(filename, 'rU')
    for line in f:
        a = line.split()
        for word in a:
            if(word > 1):
                word += 1
                print(word)
        # print(line)
    # lines = f.readlines()
    text = f.read()
    print(text)
    f.close()

def main():
    File(sys.argv[1])

if __name__ == '__main__':
    main()