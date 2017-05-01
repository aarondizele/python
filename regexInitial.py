import sys, os, re

def Find(pat, text):
    match = re.search(pat, text, re.I|re.M)
    if match:
        print("It matches : " + match.group())
    else: print('Not match')

# pat = sys.argv[1]
text1 = 'Papa part au travail, maman reste a la maison'
text2= 'c.lled piiing much better that : xyzgs'
pat1 = r'c\.l'
pat2 = 'x..g'
text3= 'blah :cat :1     2   3 blah blah blah'
pat3= r':\w\w\w'
pat4= r'\d\d\d'
pat5= r"\d\s*\d\s*\d"
pat6= r':\w+'
text4 = 'blah aldi.zele@gmail.com yotta foo@bar'
pat7= r'\w+@\w+'
pat8= r'[\w.]+@[\w.]+'
pat9= r'([\w.]+)@([\w.]+)'
Find(pat8, text4)
