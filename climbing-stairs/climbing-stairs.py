class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        dp = [-1 for i in range(n+1)]
        return self.helper(n, dp)
        
        
    def helper(self, n, dp):
        
        if n == 0:
            return 1
        
        if n < 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        ways = self.helper(n-1, dp) + self.helper(n - 2, dp)  
        
        dp[n] = ways
        
        return dp[n]
    
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n == 0:
        #     return 1
        # if n < 0:
        #     return 0
        # distinctWays = self.climbStairs(n-1) + self.climbStairs(n-2)
        # return distinctWays
        