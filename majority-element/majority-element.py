class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorElement = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                majorElement = nums[i]
                count += 1
            else:
                if nums[i] == majorElement:
                    count += 1
                else:
                    count -= 1
        return majorElement
        