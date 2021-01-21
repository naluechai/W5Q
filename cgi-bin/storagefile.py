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
		writeData = open('data.txt','a+')
		writeData.write(str(number_input))  # Add number
		writeData.write("    "+ time.ctime())  # Add time
		writeData.write("\n")
		writeData.close()
	except:	
		print("<h1>"+"Please enter only number!"+"</h1><br>")  # Show when enter alphabet

def read_temperature_file():
	# Read file to web page
	readData = open(file_name,'r')
	temperatureList=[]#list of temperature
	dateList=[]#list of date
	rawData = []#list to collect raw data
	for i in readData:#assign data to list 
		rawData.append(i)
	readData.close()
	rawData.sort(key=get_temp,reverse=True)#sort data Max to min number temperature

	for i in rawData:#seperate sorted data to 2 list
	    temperatureList.append(float(i[0:5]))
	    dateList.append(i[5:-5])
	    
	print("In File:")
	
	# Show table
	print("<table>")
	print("<tr>")
	print("<th>Date</th>")
	print("<th>Templature(C)</th>")
	print("</tr>")
	#loop show data 
	for i in range(len(temperatureList)):
		print("<tr>")
		print("<td>>"+dateList[i]+"</t1d>")
		print("<td>"+str(temperatureList[i])+"</td>")
		print("</tr>")
	print("</table>")

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











