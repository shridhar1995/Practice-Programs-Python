import random

def list_ends(a):
	return [a[0], a[-1]]

if __name__ == "__main__":
	a = random.sample(range(100), 8)

	print(a)
	print(list_ends(a))