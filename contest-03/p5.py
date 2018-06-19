# coding: utf-8
a = raw_input()
b = raw_input()

cpf = 'cpf '
values = ['', '']
chars = [a, b]
cpf_size = 11

for i in xrange(len(chars)):
    value_size = 17
    dot_size = 1
    decimals = 2

    for char in chars[i]:
        if char.isdigit():
            if cpf_size > 0:
                cpf += char
                cpf_size -= 1
            else:
                if value_size > 0 and decimals > 0:
                    values[i] += char
                    value_size += 1
                    if dot_size <= 0: decimals -= 1
        elif cpf_size <= 0 and char == '.':
            if dot_size <= 0: decimals = 0
            else:
                values[i] += char
                value_size -= 1
                dot_size -= 1

print cpf
print '%.2f' % (float(values[0]) + float(values[1]))