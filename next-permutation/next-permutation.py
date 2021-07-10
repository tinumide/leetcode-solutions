class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        4 5 6 3 7 5 2 1
        4 5 6 7 3 5 2 1
        4 5 6 5 7 3 2 1
        4 5 6 5 1 2 3 7
        
        4 3 2 1
        1 2 3 4
        """
        n = len(nums)
        if n == 1:
            return nums
        
        peak = -1
        
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                peak = i + 1
        lastIdx = peak-1
        
        if peak == -1:
            i = 0
            j = n-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
        
        for i in range(peak+1, n):
            if nums[i] > nums[lastIdx] and nums[i] < nums[peak]:
                peak = i
                
        nums[lastIdx], nums[peak] = nums[peak], nums[lastIdx]
        
        nums[lastIdx+1: n] = sorted(nums[lastIdx+1: n])
        
        return nums
            
                
        