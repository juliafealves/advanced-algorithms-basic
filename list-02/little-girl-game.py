# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Little Girl and Game

word = raw_input()

all_letters = set(word)
letter_palindrome = 0
once_odd = True

for letter in all_letters:
    amount_letter = word.count(letter)

    if amount_letter % 2 == 0:
        letter_palindrome += amount_letter
    else:
        if once_odd:
            letter_palindrome += amount_letter
            once_odd = False
        elif amount_letter - 1 > 0:
            letter_palindrome += amount_letter - 1

player_win = abs(len(word) - letter_palindrome)

if player_win % 2 == 0:
    print 'First'
else:
    print 'Second'