def fibonacci(n = 10):
	a = [1,1]
	while len(a) < n:
		i = len(a)
		a.append(a[i-2] + a[i - 1])
	return a

if __name__ == "__main__":
	n = int(input('Enter the length of Fibonacci series to be printed :- '))

	print(fibonacci(n))