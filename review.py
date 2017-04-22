import random
import sys
import os
import math
import vector2d
from vector2d import Vector2D

'''
I'm a comment
'''

# name = sys.argv[1]
# one = 5
# two = 2
## I'm also a comment
# print('App works '+name)
# print('20 // 2 = ',(20//2))

# quote = "\"Always remember you are unique"
# print(quote)

# multi_line_quote = '''I\'m a multi
# line quot'''

# print('\n'*5)

###List

# to_do_list = ['Happier', 'Perfect', 'Shape of you', 'Bibia ye']
# print(to_do_list)
# to_do_list.insert(1, 'James Arthur')
# print(to_do_list)
# to_do_list.remove('Happier')
# print(to_do_list)
# to_do_list.remove(0) #### can work because there aren't value 0 inside to_do_list
# print(len(to_do_list))
# print(max(to_do_list))
# print(min(to_do_list))
# pi_tuple = (3,1,4,1,5,9)
# print(pi_tuple)
# new_list = list(pi_tuple)
# print(new_list)
# new_tuple = tuple(new_list)
# print(new_tuple)
# print(len(new_tuple))

# for x in range(0,10):
    # print(x+ '\t')
# def Random():
#     random_num = random.randrange(0,100)
#     print(random_num)

#     while((random_num != 50) or (random_num != 10)):
#         random_num = random.randrange(0,100)
#         print(random_num)

# def main():
#     Random()

# if __name__ == '__main__':
#     main()


# print("What's your name?")

# name = sys.stdin.readline()
# print('Hello '+ name)

#myList = "Je viens d'apprendre les choses bizzares en anglais qui pourra me permettre d'approfondir mes connaissances"

# print(myList.strip())
# print(myList.join("-")) ### for list

# myFile = open("webdesign_lesson", "r+")
# # file_wrote =  myFile.write(bytes("Je suis chez moi\n"))
# try:
#     for line in myFile:
#         print(line)
# except IOError:
#     print("File cannot be read")
# finally:
#     print("File is opened")

# # print(myFile.readlines())
# print(myFile.name)
# print(myFile.mode)

# myFile.close()


# class Animal:
#     __name = None
#     __height = 0
#     __weight = 0
#     __sound = 0

#     def __init__(self, name, height, weight, sound):
#         self.__name = name
#         self.__height = height
#         self.__weight = weight
#         self.__sound = sound
    
#     def set_name(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name

#     def set_height(self, height):
#         self.__height = height
#     def get_height(self):
#         return self.__height

#     def set_weight(self, weight):
#         self.__weight = weight
#     def get_weight(self):
#         return self.__weight

#     def set_sound(self, sound):
#         self.__sound = sound
#     def get_sound(self):
#         return self.__sound
    
#     def get_type(self):
#             print("Animal")

#     def toString(self):
#         return "{} is {} cm tall and {} kilograms and says {}" .format(self.__name, self.__height, self.__weight, self.__sound)

# # cat = Animal("Cat", 123, 4, "Mhiaw")
# # print(cat.toString())
# # print(cat.get_height()," cm")
# # print(cat.get_weight()," kilograms")
# # print(cat.get_name(), "'s animal")
# # print(cat.get_sound(), " his sound")

# class Dog(Animal):
#     __name = None
#     __height = 0
#     __weight = 0
#     __sound = 0
#     __owner = None

#     def __init__(self, name, height, weight, sound, owner):
#         super(Dog, self).__init__(name, height, weight, sound)
#         self.__owner = owner

#     def set_owner(self, owner):
#         self.__owner = owner
#     def get_owner(self):
#         return self.__owner
    
#     def get_type(self):
#         print("Sub Animal")
        
#     def toString(self):
#         return "{} is {} cm tall and {} kilograms and says {} and {} his owner" .format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)

# owner = input("Enter owner name : ")
# # owner = sys.stdin.readline()

# rabbit = Dog("Rabbit", 120, 54, "TokTokToko", owner)
# print(rabbit.toString())


# nums = []
# for x in range(0,10):
#     nums.append(x)

# print(nums)

# services = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}

# for x in sorted(services.keys()):
#     run = "Keys : ", x ,"=> ", services[x]
#     print(run)

# name = input("Enter your name please: ")
# print("Hello "+ name.lower())
# print("Hello "+ name.capitalize())

# one = int(input("Enter a first number : "))
# two = int(input("Enter a first number : "))
# print("Somme equal : ", one/two)
# print("The difference is : ", str(one/two))


# x = 3
# y = 0
# intersLeft = x

# while(intersLeft > 0):
#     y = y + x
#     intersLeft = intersLeft - 1
#     print(y)


# try:
#     number = float(input("Enter a number : "))
#     number = math.fabs(number)
#     print(number)
# except:
#     print("You did not enter a correct number")

# class MyClass:
#     number = 0
#     name = ""

# def Main():
#     me = MyClass()
#     me.number = 190
#     me.name = "Draps"

#     newStudent = MyClass()
#     newStudent.number = 230
#     newStudent.name = "Patrick"

#     empty = MyClass()

#     print("Name : ", me.name, ", Favorite number : " ,me.number)
#     print("Name : ", newStudent.name, ", Favorite number : " ,newStudent.number)





     

# class Pet:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         # raise NotImplementedError("Subclass must implement abstract method")
#         return "peeeeet"
   
# class Cat(Pet):

#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def talk(self):
#         return "Meowww"


# class Dog(Pet):

#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def talk(self):
#         return "wooofff"


# pets = [Pet("Tuto", 2), Cat("Roga", 3), Dog("Milou", 5)]

# for pet in pets:
#     print("Name: "+pet.name+" , Age: "+str(pet.age)+" and says: "+pet.talk())

# print(cat.name , cat.age)
# print(pet.name , pet.age)
# print("Is Pet instance of Cat? "+str(isinstance(pet,Cat)))
# print("Is Pet instance of Cat? "+str(isinstance(cat,Pet)))



# class Reverse:

#     def __init__(self, name):
#         self.name = name
#         self.index = len(name)
    
#     def __iter__(self): ### iterator
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.name[self.index]

# name = input("Enter a word : ")
# rev = Reverse(name)

# for char in rev:
#     print(char)

# def Last(s):
#     return s[-1]

# a = "Laxis"
# print(sorted(a, key=Last))

# def Reverse(data):
#     for index in range(len(data)-1, -1, -1): ##starting in -1, stopping iteration in -1 and -1 step
#         yield data[index]

# data = Reverse("Laxis")
# for char in data:
#     print(char)
# other = "precieuse"
# print(list(other[i]           for i in range(len(other)-1, -1, -1)))


# def Main():
#     # vec = vector2d.Vector2D(5,6)
#     vec = Vector2D(5,6)
#     print(vec)
#     print("X: "+str(float(vec.x)))
#     print("Y: "+str(float(vec.y)))











# if __name__ == "__main__":
#     Main()