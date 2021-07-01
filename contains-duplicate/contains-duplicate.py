from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqMap = defaultdict(int)
        
        for i in range(len(nums)):
            freqMap[nums[i]] += 1
        
        if len(freqMap) == len(nums):
            return False
        else: 
            return True
            
        