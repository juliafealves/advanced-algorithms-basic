
def divisors(number):
    square_root = int(sqrt(number))

    for i in xrange(1, square_root + 1):
        if number % i == 0 and i * i != number:
            print i
            print number / i
        if (number % i == 0 and i * i == number): print i


def is_prime(number):
    if number <= 1: return False
    if number == 2: return True
    if number % 2 == 0: return False

    for n in xrange(3, int(sqrt(number)), 2):
        if number % n == 0: return False

    return True
