#!/usr/bin/python3
import cgi, cgitb ,timeit
print("Content-type: text/html\r\n\r\n") 
print("<html><head><style>")
print("td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}")
print("</style></head>")
print("<body>")
print("<form method = 'post' ")
print("<input type='submit' value='Enter' />") 
print("<p>Input Number: <input type='text' name='number_message'/></p>") 
print("<input type='submit' value='Enter' />") 
print("</form>")
form = cgi.FieldStorage() 
number_input = form.getvalue('number_message')
def factorial(n):
    fac = 1 
    for i in range(n):
        fac *= (i+1)
    print(fac)
if number_input != None:
    print('<p>result</p>')
    print('<p>')
    try:
        num = int(number_input)
    except:
        print('please enter a number')
    if num >= 0:
        start = timeit.default_timer()
        factorial(num)
        stop = timeit.default_timer()
    else:
        print('negative factorial not define')
    print('</p><hr>')
    print('<p>',num,'! using',stop-start,'second </p>')
print("</body></html>") 
