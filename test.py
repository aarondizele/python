import random
# samp = iter('Samp')
# print(next(samp))
# print(next(samp))

# class Alphabet:

#     def __init__(self):
#         self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         self.index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.letters) - 1:
#             raise StopIteration
#         self.index += 1
#         return self.letters[self.index]
#
# alpha = Alphabet()
# for letter in alpha:
#     print(letter, end=" ")

# class FibGenerator:
#     def __init__(self):
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         fibnum = self.first + self.second
#         self.first = self.second
#         self.second = fibnum
#         return fibnum
#
# fibSeq = FibGenerator()
#
# for i in range(10):
#     print("Fib :", next(fibSeq))

### List comprehension
# print([x*y for x in range(1, 3) for y in range(11,16)])

# print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

# multilist = [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
# print([col[0] for col in multilist])
# print([multilist[i][i] for i in range(len(multilist))])



# print(list(map((lambda x,y:x+y),[8,6,3],[3,2,3])))

# attack = {'quick': (lambda:print("QUick attack")),
#         'hearth': (lambda:print("Hearth attack")),
#           'miss': (lambda:print("Missed attack"))
#         }
# attack['hearth']()




