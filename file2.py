import random
import os

# list1 = ['Rabbit', 'Cow','Horse', 'Chiken']
#
# with open("awesome.txt", mode="a", encoding="utf-8", newline="") as myFile:
#     for i in range(10):
#         write_ = random.choice(list1) + '\r\n'
#         myFile.write(write_)
#     myFile.write("\n ------------------------- \n")
#     print("Writing done")

with open('awesome.txt') as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break
        print("Line", lineNum, " : ", line, end="")
        lineNum += 1


# namefile = input("Rename file : ")
# os.rename("awesome.txt", namefile)
# print("File renamed!")
# os.mkdir("folder")
# print("Folder created!")
# print("Current directory : ", os.getcwd())
# os.chdir("/..")
# print("Current directory : ", os.getcwd())



