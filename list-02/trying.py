# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Little Girl and Game

word = raw_input()

all_letters = set(word)
letter_palindrome = 0
one_impar = True
teste = {}

for letter in all_letters:
	amount_letter = word.count(letter)
	teste[letter] = amount_letter
	
	if amount_letter % 2 == 0:
		letter_palindrome += 1
	elif one_impar:
		letter_palindrome += 1
		one_impar = False

player_win = len(all_letters) - letter_palindrome

if player_win % 2 == 0 and player_win != 0:
	print 'Second'
else:
	print 'First'

print teste
print len(teste)
