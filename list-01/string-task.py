# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: A. String Task

string = raw_input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ''

for letter in string:
    if not (letter in vowels):
        consonants += '.' + letter

print consonants

