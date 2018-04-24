# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Little Girl and Game


def is_palindrome(word):
    return word == word[::-1]


def sum_letter(string):
        all_letters = set(string)

        for letter in all_letters:
            amount_letters[letter] = string.count(letter)


def get_letter_removed():
    smaller = min(amount_letters.values())

    for letter, amount in amount_letters.iteritems():
        if amount == smaller:
            amount_letters[letter] -= 1
            if amount_letters[letter] <= 0:
                amount_letters.pop(letter)

            return letter


def remove_letter(word, i, j):
    substring = word[i:j]

    if len(amount_letters) == 0:
        sum_letter(substring)

    letter_removed = get_letter_removed()
    substring = substring.replace(letter_removed, '', 1)

    return word[:i] + substring + word[j:]


word = raw_input()

i = 0
j = len(word) - 1

player = 1
amount_letters = {}

while not is_palindrome(word):
    if word[i] != word[j]:
        player += 1
        word = remove_letter(word, i, j + 1)
        j -= 1
    else:
        i += 1
        j -= 1

if player % 2 == 0:
    print "Second"
else:
    print "First"

print word
