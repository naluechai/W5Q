import time
def factorial(n):
	if (n != 1) :
		return n*factorial(n-1)
	elif (n == 1):
		return 1
		
def factorial2(n):
	start = time.time()
	fact = n
	result = 1
	while(n != 1):
		result = result*n
		n -=1
	print (result)
	end = time.time()
	
	print("factorial",fact)
	print("time:",end - start)
	
		
def factorial3(n):
	result = 1
	i = 1
	while(i != n+1):
		result = result*i
		i +=1
	return result
	
factorial2(125000)

