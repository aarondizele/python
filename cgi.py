#!/usr/bin/python3
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html><body>")


form = cgi.fieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h3>Hello "+name+"! Thanks for using my script!</h1><br>")
if form.getvalue("name"):
    print("<p> Yay! I'm happy too!</p>")
if form.getvalue("name"):
    print("<p>Oh no! Why are you sad? </p>")


print("<form methode='post' action='cgi.py' ")
print("<p>Name: <input type='text' name='name' />")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")

print("</body></html>")