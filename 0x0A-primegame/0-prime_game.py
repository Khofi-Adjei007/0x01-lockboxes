#!/usr/bin/python3
"""Module containing the isWinner function for the Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list): A list where each element
    represents the upper bound
    of the set of numbers for a particular round.

    Returns:
    str: "Winner: Maria" if Maria wins more rounds,
    "Winner: Ben" if Ben wins
    more rounds, or None if the result is a tie.
    """

    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while True:
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"

    return None


def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """
    Generates a list of prime numbers within a given range.

    Parameters:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    list: A list of prime numbers between start and end.
    """
    return [n for n in range(start, end + 1) if is_prime(n)]
