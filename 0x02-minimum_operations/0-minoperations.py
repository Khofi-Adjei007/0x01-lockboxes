import math

def minOperations(n):
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
