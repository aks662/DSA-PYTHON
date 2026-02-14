class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        st=0
        e=n-1
        ans=True
        # print(s[-1])
        while st<(e):
            
            while not s[st].isalnum() and st<e:
                st+=1
            while not s[e].isalnum() and st<e:
                e-=1
            if s[st].lower()!=s[e].lower():
                ans=False
                break
            e-=1
            st+=1
        return (ans)