#!/usr/bin/python3
import cgi, cgitb 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>")

form = cgi.FieldStorage() 
number = form.getvalue('input')


# Form for input
print("<form method = 'post' ")
print("<p>Input: <input type='text' name='input' /></p>") 
print("<input type='submit' value='Submit' />") 
print("</form>  ")

# Check number is not alphabet
try:
	int(number)
	isNumber = True
	str(number)
except:
	isNumber = False
	
# Add text in file
if (isNumber == True):
	# Write if number is not alphabet
	f = open('data.txt', 'a+')
	f.write(number)
	f.write("<br>")
	f.close()
elif (number != None):
	print("<h1>"+"Please enter only number!"+"</h1><br>")  # Show when enter alphabet

# Read file to web page
r = open('data.txt', 'r')
s = r.read()
print("In File:")
print("<h1>"+s+"</h1><br>")
r.close()

print("</body></html>") 

