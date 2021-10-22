class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        4 1 4
        4 2 16
        4 3 64
        4 4 256
        4 5 1024
        '''
        if n <= 0:
            return False
        
        if  n == 1:
            return True
        
        if n % 4 == 0:
            return self.isPowerOfFour(n//4)
        else:
            return False
        