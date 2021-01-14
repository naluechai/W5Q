#!/usr/bin/python3
import cgi, cgitb 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>")
form = cgi.FieldStorage() 
number = form.getvalue('input')

print("<form method = 'post' ")
print("<p>Input: <input type='text' name='input' /></p>") 
print("<input type='submit' value='Submit' />") 
print("</form>  ")
print("Read File Have :")


f = open('data.txt', 'a+')
f.write(number)
s = f.read()
print(s)
f.close()

print("</body></html>") 

