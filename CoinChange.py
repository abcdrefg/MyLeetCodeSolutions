class Solution:
    def coinChange(self, coins, amount: int) -> int:
        num_of_coins = 0
        coins.sort()
        for i in reversed(range(len(coins))):
            num_of_coins += amount // coins[i]
            amount = amount % coins[i]
        if amount > 0:
            return -1
        return num_of_coins


print(Solution().coinChange([186,419,83,408], 6249))