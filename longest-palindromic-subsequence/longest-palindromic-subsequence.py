class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        start = 0
        end = len(s) - 1
        dp = [[-1 for i in range(len(s))] for i in range(len(s))]
        return self.helper(s, start, end, dp)
    
    def helper(self, s, start, end, dp):
        
        if start == end:
            return 1
        
        if start > end:
            return 0
        
        if dp[start][end] != -1:
            return dp[start][end]
        
        if s[start] == s[end]:
            dp[start][end] = 2 + self.helper(s, start+1, end-1, dp)
        else:
            palindrome1 = self.helper(s, start+1, end, dp)
            palindrome2 = self.helper(s, start, end-1, dp)
            dp[start][end] = max(palindrome1, palindrome2)
            
        return dp[start][end]
        