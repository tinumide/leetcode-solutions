class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashMap = {}
        
        for i in range(1, n+1):
            hashMap[i] = 0
            
        for i in range(len(trust)):
            hashMap[trust[i][0]] -= 1
            hashMap[trust[i][1]] += 1
        
        for v, e in hashMap.items():
            if e == n-1:
                return v
        
        return -1
        