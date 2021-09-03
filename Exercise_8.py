# ROCK PAPER SCISSOR

def winner(player_a, player_b):
	if player_a == player_b:
		return(0)
	else:
		if player_a == 'ROCK':
			if player_b == 'PAPER':
				return('PLAYER B')
			elif player_b == 'SCISSOR':
				return('PLAYER A')

		elif player_a == 'PAPER':
			if player_b == 'ROCK':
				return('PLAYER A')
			elif player_b == 'SCISSOR':
				return('PLAYER B')

		else:
			if player_b == 'PAPER':
				return('PLAYER A')
			elif player_b == 'ROCK':
				return('PLAYER B')


if __name__ == "__main__":
	from termcolor import colored
	result = 0
	while(result == 0):
		player_a = input('PLAYER A ENTER ROCK / PAPER / SCISSOR :- \n')
		player_b = input('\nPLAYER B ENTER ROCK / PAPER / SCISSOR :- \n')

		result = winner(player_a, player_b)

		if result != 0:
			print(colored('\n' + result + ' is the winner!!\n', 'green'))
		else:
			print(colored("\nIt's a TIE. Play Again!! \n", 'red'))

