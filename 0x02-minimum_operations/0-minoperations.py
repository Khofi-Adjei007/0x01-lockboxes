#!/usr/bin/python3

"""
Module: min_operations

Function to calculate the fewest number of operations
needed to obtain `n` 'H' characters
in a text file using "Copy All" and "Paste".
"""

import math

def minOperations(n):
    
    """
    Calculate the minimum operations needed
    to generate `n` 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations.
        Returns 0 if `n` is impossible to achieve.

    Explanation:
        Uses dynamic programming to efficiently compute
        the minimum operations by considering
        all possible ways to copy and paste
        substrings to form `n` 'H' characters.

    Raises:
        ValueError: If `n` is less than 1.

    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 + (i // j - 1))
                if j != 1:
                    dp[i] = min(dp[i], dp[i // j] + j)
    
    return dp[n] if dp[n] != float('inf') else 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

