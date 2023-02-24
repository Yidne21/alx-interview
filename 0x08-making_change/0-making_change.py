#!/usr/bin/python3
'''
A modul which solves coin problem
'''


def makeChange(coins, total):
    '''
    A function which returns fewest number of coins needed to
    meet a given total coin number if total is not less than 0
    '''
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
