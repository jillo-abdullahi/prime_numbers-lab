def primeNumbers(test):
	prime_numbers = []
	for num in range(2,test):
		if num > 1:
			for i in range(2,num):
				if(num%i) == 0:
					break
			else:
				prime_numbers.append(num)
	return prime_numbers

