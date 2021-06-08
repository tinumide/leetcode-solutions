class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(0, len(s)-1, s)
    
    def helper(self, start, end, s):
        if start >= end:
            return
        s[start], s[end] = s[end], s[start]
        
        return self.helper(start+1, end-1, s)