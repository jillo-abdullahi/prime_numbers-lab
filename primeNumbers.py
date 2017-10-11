def primeNumbers(test):
	prime_numbers = []
	#Checking for valid inputs
	if test < 1:
		return []
	if isinstance(test, list):
		raise TypeError("test cannot be a list") 
	if isinstance(test, dict):
		raise TypeError("test cannot be dictionary") 
	else:
		for num in range(2,test):
			#Check for prime for values greater than 1
			for i in range(2,num):
				if(num%i) == 0:
					break
			else:
				prime_numbers.append(num)
	return prime_numbers


