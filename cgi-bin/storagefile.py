#!/usr/bin/python3
import cgi, cgitb 
import time
import random

def get_temp(data):
	return float(data[0:5])

def head_HTML():
	print("Content-type: text/html\r\n\r\n") 
	print("<html><head><style>")
	print("td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}")
	print("</style></head>")
	print("<body>")

def temperature_input_form():
	# Form for temperature input
	print("<form method = 'post' ")
	print("<input type='submit' value='Enter' />") 
	print("<p>Input Number: <input type='text' name='number_message'/></p>") 
	print("<input type='submit' value='Enter' />") 
	print("</form>")

def add_temperature_in_file():
	# Add text if is not a alphabet
	try:
		# Check number is not alphabet
		float(number_input)
		isNumber = True
		str(number_input)
	except:
		isNumber = False
		
	# Add text in file
	if (isNumber == True):	
			# Write if number is not alphabet
			f = open(file_name,'a+')
			f.write(number_input)  # Add number
			f.write("    "+ time.ctime())  # Add time
			#f.write("<br>")
			f.write("\n")
			f.close()
	elif (number_input != None):
		print("<h1>"+"Please enter only number!"+"</h1><br>")  # Show when enter alphabet

def read_temperature_file():
	# Read file to web page
	readed = open(file_name,'r')
	role=[]#list of templature
	date=[]#list of date
	temp = []
	for i in readed:
		temp.append(i)
	temp.sort(key=get_temp,reverse=True)

	for i in temp:
	    role.append(float(i[0:5]))
	    date.append(i[5:-5])
	    
	print("In File:")
	
	# Show table
	print("<table>")
	print("<tr>")
	print("<th>Date</th>")
	print("<th>Templature(C)</th>")
	print("</tr>")
	print("<tr>"+"<td>>"+str(random.randrange(0,10))+"</t1d>" + "<td>"+str(random.randrange(0,10))+"</td>"+"</tr>")  # test random

	for i in range(len(role)):
		print("<tr>")
		print("<td>>"+date[i]+"</t1d>")
		print("<td>"+str(role[i])+"</td>")
		print("</tr>")
		
	print("</table>")
	readed.close()

def tail_HTML():
	print("</body></html>") 

# Decalre varible
form = cgi.FieldStorage() 
number_input = form.getvalue('number_message')

head_HTML()
temperature_input_form()  # Input form
file_name = 'data.txt'
add_temperature_in_file()  # Write input in file
read_temperature_file()  # Read file
tail_HTML()











