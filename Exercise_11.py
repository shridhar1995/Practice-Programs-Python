def primality(n):
	if n == 0:
		return('Number is not a prime number!!')
	elif n == 1:
		return('Number is not a prime number!!')
	elif n == 2:
		return('Number is a prime number!!')
	for i in range(2,n):
		if n % i == 0:
			return('Number is not a prime number!!')
	return('Number is a prime number!!')


if __name__ == "__main__":
	n = int(input('Enter a number :- '))
	print(primality(n))
