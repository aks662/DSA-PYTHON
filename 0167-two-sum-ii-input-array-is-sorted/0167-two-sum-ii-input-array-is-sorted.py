class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        s=len(n)
        l=0
        r=s-1
        ans=0
        while l<r:
            ans=n[l]+n[r]
            
            if ans==t:
                return (l+1,r+1)
                break
            elif ans>t:
                r-=1
            else:
                l+=1
        return False