class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1,2,1,3,5,6,4]
        0 6 3
        4 6 
        """
        n = len(nums)
        
        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[n-1] > nums[n-2]:
            return n-1
        
        left = 1
        right = n - 2
        
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid-1] > nums[mid]:
                right = mid-1
                
            else:
                left = mid+1
                
        return left
            
            
        