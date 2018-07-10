# coding: utf-8
dp = [0, 1]

def fibonacciDP(number):
    while len(dp) < number + 1: dp.append(0)

    if number <= 1: return number
    else:
        if dp[number - 1] == 0: dp[number - 1] = fibonacciDP(number - 1)
        if dp[number - 2] == 0: dp[number - 2] = fibonacciDP(number - 2)

        dp[number] = dp[number - 2] + dp[number - 1]

        return dp[number]

n = int(raw_input())
fibonacciDP(n)
for i in xrange(n): print dp[i],