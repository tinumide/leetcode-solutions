class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ans = self.helper(x, abs(n))
        
        if n < 0:
            return 1/ans
        
        return ans
    
    def helper(self, x, n):
        
        if n == 0:
            return 1
        
        half = self.helper(x, n//2)
        
        if n % 2 == 0:
            return half * half
        
        return half * half * x
        