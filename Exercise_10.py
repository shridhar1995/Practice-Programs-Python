import random

a = random.sample(range(100), 7)
b = random.sample(range(100), 9)

c = [i for i in a if i in b]

print(a)
print(b)
print(c)