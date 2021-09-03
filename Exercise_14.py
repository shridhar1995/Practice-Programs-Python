def duplicate_removal(a):
	return(list(set(a)))

def dup_removal(a):
	ind = []
	for i in range(0,len(a)):
		for j in range(0,len(a)):
			if a[i] == a[j]:
				if i == j:
					continue
				else:
					ind.append(j)
	print(list(set(ind)))
	return(a)


if __name__ == "__main__":
	a = [1,2,3,4,5,3,2,1,3,4,4,4]

	print(dup_removal(a))