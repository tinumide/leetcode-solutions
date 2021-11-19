from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        4329
        4330
        
        9999
       10000
        
        4399
        4400
        
        convert to int
        left shift integer by 1
        convert back to arr of digits 
        return array of digits
        '''
        multiplier = 1
        idx = len(digits) - 1
        integer = 0
        
        ans = deque([])
        
        while idx >= 0:
            integer = (digits[idx] * multiplier) + integer
            multiplier *= 10
            idx -= 1
        
        new_integer = integer + 1
        
        while new_integer:
            ans.appendleft(new_integer % 10)
            new_integer = new_integer // 10
        
        return list(ans)
            
        
            
        
        
        