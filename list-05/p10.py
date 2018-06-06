# coding: utf-8
def fatorial(n, array):
    if n == 0 or n == 1:
        return 1
    else:
        array[n] = n * fatorial(n - 1, array)
        return array[n]

factoriais = [1] * 61
fatorial(60, factoriais)
n, m, t = map(int, raw_input().split())
groups = 0
b = 4
g = t - b

while g != 0:
    groups += (factoriais[n]/(factoriais[b] * factoriais[n - b])) * (factoriais[m]/(factoriais[g] * factoriais[m - g]))
    g -= 1
    b += 1

print groups
