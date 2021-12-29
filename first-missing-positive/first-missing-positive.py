class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        1, 2, 0
        '''
        n = len(nums)
        
        for i in range(n):
            
            while 1 <= nums[i] <= n:
                
                pos = nums[i] - 1
                
                if nums[pos] != nums[i]:
                    
                    nums[i], nums[pos] = nums[pos], nums[i]
                else:
                    break
                    
        for i in range(n):
            
            if nums[i] != i + 1:
                
                return i + 1
        return n + 1