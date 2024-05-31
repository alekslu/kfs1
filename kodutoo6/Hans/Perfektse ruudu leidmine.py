class Solution(object):
    def numSquares(self, n):
        
        # Initialize a list to store the minimum number of perfect squares required for each number up to n
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Initialize the value for dp[i] to i, as it's the worst case (when n is the sum of i 1s)
            dp[i] = i
            j = 1
            while j * j <= i:
                # For each square number j * j less than or equal to i, update dp[i] if needed
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
