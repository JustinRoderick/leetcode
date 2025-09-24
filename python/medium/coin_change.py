# 322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                dif = i - coin
                if dif < 0:
                    continue
                min_coins[i] = min(min_coins[i], min_coins[dif] + 1)

        return -1 if min_coins[amount] == float('inf') else min_coins[amount]