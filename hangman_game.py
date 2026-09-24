import random
import sys
words = ('regret', 'brutality', 'carpenter', 'denmark', 'plumber', 'fertility', 'greedy', 'computer', 'device', 'entrepreneur', 'fidelity', 'generosity', 'humanity', 'intimacy', 'youth', 'kiwi', 'longevity', 'mediocrity', 'necessity', 'opportunity', 'procrastinate', 'quantity', 'relationship', 'superficial', 'technology', 'uniform', 'vascularized', 'chess', 'zoo', 'ambitious', 'cheek', 'complex', 'dictionary', 'extroverted', 'happiness', 'kindness', 'ability', 'important', 'judgment', 'language', 'maturity', 'nationality', 'organism', 'perspective', 'kilometer', 'responsibility', 'overrated', 'transparent', 'university', 'vulnerability', 'xenophobia', 'retired', 'bibliography', 'characteristic', 'development', 'exponential', 'fragmented', 'napkin', 'hereditary', 'independent', 'jabuticaba', 'lubricant', 'meteorology', 'neurotransmitter')
chosen_word = []
hidden_word = []
hangman = {'head': ' ', 'torso1': ' ', 'torso2': ' ', 'right_arm': ' ', 'left_arm': ' ', 'right_leg': ' ', 'left_leg': ' '}
wrong_guesses = []

def play_again():
	while True:
		print('[1] - Play Again.\n[2] - Exit. ')
		option = int(input('-: '))
		if option == 1:
			break
		elif option == 2:
			sys.exit()
		else:
			print('\033[1;38;5;9mERROR: Invalid option.\033[0m')

def add_hyphen():
	for c in range(0, len(chosen_word)):
		hidden_word.append('-')

def add_letter():
	for index, character in enumerate(chosen_word):
		if character == letter:
			hidden_word[index] = letter

def add_word():
	rand = random.randint(0, len(words) - 1)
	for char in words[rand]:
		chosen_word.append(char)
				
def add_hangman():
	if len(wrong_guesses) == 1:
		hangman['head'] = 'O'
	elif len(wrong_guesses) == 2:
		hangman['torso1'] = '|'
	elif len(wrong_guesses) == 3:
		hangman['torso2'] = '|'
	elif len(wrong_guesses) == 4:
		hangman['right_arm'] = '/'
	elif len(wrong_guesses) == 5:
		hangman['left_arm'] = '\\'
	elif len(wrong_guesses) == 6:
		hangman['right_leg'] = '/'
	elif len(wrong_guesses) == 7:
		hangman['left_leg'] = '\\'
	print('=' * 30)
	print('  |--------| ')
	print('  |        !')
	print(f'  |        {hangman['head']}')
	print(f'  |       {hangman['right_arm']}{hangman['torso1']}{hangman['left_arm']}')
	print(f'  |        {hangman['torso2']}')
	print(f' /|\\      {hangman['right_leg']} {hangman['left_leg']}')
	print('/ | \\')
	print('=' * 30)
 	
def reset_game():
	hangman.update({'head': ' ', 'torso1': ' ', 'torso2': ' ', 'right_arm': ' ', 'left_arm': ' ', 'right_leg': ' ', 'left_leg': ' '})
	wrong_guesses.clear()
	chosen_word.clear()
	hidden_word.clear()
	add_word()
	add_hyphen()
	play_again()
						
add_word()
add_hyphen()
while True:		
	add_hangman()	
	print(*hidden_word)
	letter = input('Enter a letter: ').strip().lower()
	add_letter()
		
	if letter not in chosen_word and letter not in wrong_guesses and len(letter) == 1 and letter.isalpha():
		wrong_guesses.append(letter) 
		
	if len(wrong_guesses) == 7:
		add_hangman()
		print(*chosen_word)
		print('\033[1;31mYou lost!\033[0m')
		reset_game()
			
	if hidden_word.count('-') == 0:
		add_hangman()
		print(*hidden_word)
		print('\033[1;32mCongratulations, you got it right!\033[0m')
		reset_game()