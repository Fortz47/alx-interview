#!/usr/bin/python3

""" Dynamic programming and greedy algorithms:
    the coin change problem
"""


def makeChange(coins, total):
    """ Determine the fewest number of coins needed
        to meet total
    """
    if total <= 0:
        return 0

    num_of_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = total // coin
        num_of_coins += r
        total -= r * coin
        if total == 0:
            return num_of_coins
    return -1
