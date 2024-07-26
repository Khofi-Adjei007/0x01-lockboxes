#!/usr/bin/python3

"""Change-making module.
"""


def makeChange(coins, total):

    """Determine the minimum number of coins needed
    to make up a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount to make.

    Returns:
        int: The minimum number of coins required to reach the total,
              or -1 if the total cannot be reached with the given coins.
    """
    if total <= 0:
        return 0

    # Initialize an array to keep track of the minimum number of
    # coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Compute the minimum number of coins needed for the current amount
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins needed for the total amount,
    # or -1 if it's not possible to form the total with the given coins
    return min_coins[total] if min_coins[total] != float('inf') else -1
