#!/usr/bin/python3

"""
Module: min_operations

Function `minOperations` calculates the minimum
operations to achieve `n` 'H' characters
using "Copy All" and "Paste".
"""

def minOperations(n):
    """
    Calculate minimum operations to achieve
    `n` 'H' characters.

    Args:
        n (int): Desired number of 'H' characters.

    Returns:
        int: Minimum number of operations.

    Explanation:
        Recursively computes minimum operations by
        dividing `n` by divisors
        until `n` is reduced to 1.

    Note:
        Returns 0 if `n` is less than or equal to 1.
    """
    if n <= 1:
        return 0
    
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op

if __name__ == "__main__":
    import doctest
    doctest.testmod()
