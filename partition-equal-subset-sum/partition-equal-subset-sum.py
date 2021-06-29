class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        som = sum(nums)       # O(n)
        
        if som % 2 != 0:    # sum has to be even to find a subset sum equal to sum/2 O(1)
            return False
        
        dp = [[-1 for i in range(som//2 + 1)] for i in range(len(nums))] # for memoization
        
        return self.subsetSum(nums, som//2, 0, dp)  
    
    def subsetSum(self, nums, subsum, idx, dp):
        if subsum == 0:
            return True
        
        if idx >= len(nums) or subsum < 0:
            return False
        
        if dp[idx][subsum] != -1:
            return dp[idx][subsum]
        
        nxtSub = nums[idx]
        
        newsubSum = subsum - nxtSub
        
        isSubSet = self.subsetSum(nums, newsubSum, idx+1, dp) or self.subsetSum(nums, subsum, idx+1, dp)
        
        dp[idx][subsum] = isSubSet
        
        return dp[idx][subsum] 
        
        
        