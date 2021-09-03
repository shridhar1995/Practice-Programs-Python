import random
from termcolor import colored

guess = 0
while(guess != 'exit'):

	a = random.randint(1,9)

	guess = 0
	n = 0

	while (guess != a):

		guess = input('\nGuess the number between 1 to 9 :- ')
		n = n+1
		if guess == 'exit':
			break
		else:
			guess = int(guess)
			if guess == a:
				print(colored('\nSPOT ON!!\n', 'green'))
				print(colored('You guessed the number in ' + str(n) + 'attempts.', 'green'))
			elif guess < a:
				print(colored('\nLOW\n', 'yellow'))
			elif guess > a:
				print(colored('\nHIGH\n', 'yellow'))
