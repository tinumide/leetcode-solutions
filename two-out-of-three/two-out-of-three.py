

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
       
        hashMap = {}
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        result = []
        
        for i in chain(nums1, nums2, nums3):
            
            if hashMap.get(i):
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            
        for num, count in hashMap.items():
            if count >= 2:
                result.append(num)
        
        return result
        
        
        