class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount 
        for i in range(1, amount+1):
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i-j]+1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1