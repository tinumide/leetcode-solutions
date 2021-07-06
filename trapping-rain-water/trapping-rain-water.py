class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0 for i in range(len(height))]
        rightMax = [0 for i in range(len(height))]
        trappedWater = 0
        
        max_ = -float('inf')
        
        for i in range(len(height)):
            max_ = max(height[i], max_)
            leftMax[i] = max_
            
        max_ = -float('inf')
        
        for i in range(len(height)-1, -1, -1):
            max_ = max(height[i], max_)
            rightMax[i] = max_
        
        for i in range(1, len(height)-1):
            water = (min(leftMax[i-1], rightMax[i+1]) - height[i])
            if water > 0:
                trappedWater += water
            
        return trappedWater
            