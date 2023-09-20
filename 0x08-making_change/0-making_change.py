def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)

    # Base case: You need 0 coins to make a total of 0.
    dp[0] = 0

    # Iterate through all possible amounts from 1 to 'total'.
    for amount in range(1, total + 1):
        # Try each coin denomination.
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] <= total else -1

# Test cases


print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
