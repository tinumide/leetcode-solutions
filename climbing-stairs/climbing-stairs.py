class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        distinctWays = self.climbStairs(n-1) + self.climbStairs(n-2)
        return distinctWays
        