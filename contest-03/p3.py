# coding: utf-8
while True:
    inputs = raw_input().split()

    if inputs == ['0', '0']:
        break

    digit = inputs[0]
    number = inputs[1]
    amount_digit = number.count(digit)

    if amount_digit == 0:
        print int(number)
    else:
        new_number = ''
        count = 0
        i = 0

        while count < amount_digit:
            if number[i] == digit:
                count += 1
            else:
                new_number += number[i]

            i += 1

        new_number += number[i:]

        if new_number == '':
            print 0
        else:
            print int(new_number)