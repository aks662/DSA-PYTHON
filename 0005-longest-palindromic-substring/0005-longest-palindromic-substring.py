class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromic(s,l,r):
    
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1

            return(s[l+1:r])
        ans_even=""
        ans_odd=""
        for i in range(len(s)):
        
            even=palindromic(s,i,i+1)
            if len(even)>len(ans_even):
                ans_even=even
                
            odd=palindromic(s,i,i)
            if len(ans_odd)<=len(odd):
                ans_odd=odd
        return (ans_even if len(ans_even)>len(ans_odd) else (ans_odd))