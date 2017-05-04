import re

# allApes = re.findall("ape.", "The ape was at the apex")
#
# for i in allApes:
#     print(i)


theStr = "The ape was at the apex"

# for i in re.finditer("ape.", theStr):
#     locTuple = i.span()
#     print(locTuple)
#     print(theStr[locTuple[0]:locTuple[1]])

animalStr = "Cat rat mat pat"
animalStr = animalStr.lower()
# allAnimals = re.findall("[crmp]at", animalStr)
# allAnimals = re.findall("[c-mC-M]at", animalStr)
#
# for i in allAnimals:
#     print(i)
# # print(animalStr)

# regex = re.compile("[cr]at")
# owlFood = regex.sub("owl", animalStr)
# print(owlFood)

# randStr = "F.B.I. I.R.S. D.R.C. CIA"
# print("Matches :",len(re.findall(".\..\..\.", randStr)))


### replace comment to one line
# randStr = '''This is a long
# string that goes
# on for many lines
# '''
# print(randStr)
# regex = re.compile("\n")
# randStr = regex.sub(" ", randStr)
# print(randStr)

# randStr = "12345"
# print("Matches :",len(re.findall("\d{4}", randStr)))

# phNum = "412-564-4421"
# # if re.search("\d{3}-\d{3}-\d{3}", phNum):
# if re.search("\w{3}-\w{3}-\w{4}", phNum):
#     print("It's a phone number")
#
# if re.search("\w{1,3}", "Aaroooooon"):
#     print("Is a valid name")
# else:
#     print("Is a wrong name")


# # if re.search("\w{2,20}\s\w{2,20}","Toshio Muramatsu"):
# print("Email Matches :", len(re.findall(r"[\w._%+-]{1,20}@[\w.-]{1,20}.[A-Za-z]{2,3}", emailaddress)))

# emailList = "db@aol.com m@.com @apple.com db@.com"
#
# print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
#                                         emailList)))


# randStr = "cat cats"
# randStr = "<name>Life on Hearth</name><name>Freaking perfect</name>"
# regex = re.compile("<name>(.*?)</name>") ###lazy RE
# regex = re.compile("[cat]+s?") ### ? - 0 or 1 of preceding RE

# randStr = "@ Get this string"
# randStr = "My number is 412-555-1212 412-555-1213 412-555-1214"
# regex = re.compile(r"412-(.{8})")
# # regex = re.compile(r"412-(.*)")
#
# # regex = re.compile(r"[^@\s].*$")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)


# randStr = "412-555-1212"
#
# regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
# randStr = re.sub(regex, r"(\1) \2", randStr)
# print(randStr)

### Very important
# randStr = "https://www.youtube.com http://www.google.com"
# regex = re.compile(r"(https?://([\w.]+))")
# randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)
# print(randStr)

# #(?=expression) look ahead
# randStr1 = "One two three four"
# regex1 = re.compile(r"\w+(?=\b)")
# matches1 = re.findall(regex1, randStr1)
# for i in matches1:
#     print(i)

# #(?<=expression) look behind
# randStr1 = "1. One 2. Two 3. Three 4. Four"
# regex1 = re.compile(r"(?<=\d.\s)\w+")
# matches1 = re.findall(regex1, randStr1)
# for i in matches1:
#     print(i)

# # Look ahead and behind
# randStr1 = "<h1>I'm Important</h1><h1>So am I</h1>"
# regex1 = re.compile(r"(?<=<h1>).+?(?=</h1>)")
# matches1 = re.findall(regex1, randStr1)
# for i in matches1:
#     print(i)

# (?!expression): Negative look ahead || (?<!expression): Negative look Behind
randStr1 = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex1 = re.compile(r"(?<!\$)\d+")
matches1 = re.findall(regex1, randStr1)
matches1 = [int(i) for i in matches1]

from functools import reduce

print("Total Items {}".format(reduce((lambda  x, y: x+y),matches1)))
























































