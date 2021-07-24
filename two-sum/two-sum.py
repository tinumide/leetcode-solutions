from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            val = target-nums[i]
            if val in hash_map and hash_map[val] != i:
                return [i, hash_map[val]]
            else:
                hash_map[nums[i]] = i
        
                
            