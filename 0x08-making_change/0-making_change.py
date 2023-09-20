def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount from 0 to 'total'.
    # Initialize all values with a maximum value (total + 1) to indicate that they are not yet computed.
    dp = [total + 1] * (total + 1)

    # Base case: You need 0 coins to make a total of 0.
    dp[0] = 0

    # Iterate through all possible amounts from 1 to 'total'.
    for amount in range(1, total + 1):
        # Try each coin denomination.
        for coin in coins:
            if amount - coin >= 0:
                # Update the minimum number of coins needed for the current amount.
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value at 'total' is still the initial maximum, it means it's impossible to make change.
    return dp[total] if dp[total] <= total else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
