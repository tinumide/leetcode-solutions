class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #     1 0 0
        # 1 1 0 1 0 
        #     1 1 0
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []
        
        while i >= 0 and j >= 0:
            sum_ = int(a[i]) + int(b[j]) + carry
            if sum_ == 2:
                ans.append('0')
                carry = 1
            elif sum_ == 3:
                ans.append('1')
                carry = 1
            else:
                ans.append(str(sum_))
                carry =  0
            i -= 1
            j -= 1
            
        if i >= 0:
            
            while i >= 0:
                sum_ = int(a[i]) + carry
                if sum_ == 2:
                    ans.append('0')
                    carry = 1
                elif sum_ == 3:
                    ans.append('1')
                    carry = 1
                else:
                    ans.append(str(sum_))
                    carry =  0
                i -= 1
        elif j >= 0:
            while j >= 0:
                sum_ = int(b[j]) + carry
                if sum_ == 2:
                    ans.append('0')
                    carry = 1
                elif sum_ == 3:
                    ans.append('1')
                    carry = 1
                else:
                    ans.append(str(sum_))
                    carry =  0
                j -= 1
        if carry:
            ans.append(str(carry))
        ans = ''.join(ans)
        return ans[::-1]
        
            
                
            