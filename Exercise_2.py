n = int(input('Enter a number :: '))

if(n % 2 == 0):
	if(n % 4 == 0):
		print(str(n) + ' is a multiple of 4.')
	else:
		print(str(n) + ' is an even number.')
else:
	print(str(n) + ' is an odd number.')


num = int(input('Enter a dividend :: '))
check = int(input('Enter a divisor :: '))

if num % check == 0:
	print('Divisor divides the dividend evenly.')
else:
	print('Divisor is not a factor of Dividend.')