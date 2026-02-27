'''
You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Example 3:
Input: coins = [1], amount = 0
Output: 0
'''
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #using dynamic programming pattern
        #intializing dp array
        dp = [float('inf')]*(amount + 1)#amount may range from 0 to amount+1
        #base case
        dp[0] = 0 #to make 0 amount we need 0 coins
        #here i is amount to make,choosing coin, if this coin is used then still i-coin = amount has to be made
        #coins_needed = dp[i-coin] +1 #added 1 as we used one coin now
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >=0:
                    dp[i] = min(dp[i],dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1
        