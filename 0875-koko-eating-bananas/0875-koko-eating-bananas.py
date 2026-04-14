import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles)==1:
        #     return piles[0]
        l=1
        r=max(piles)
        ans=-1
        while l<=r:
            m=(l+r)//2

            time=0
            for i in piles:
                time+=(math.ceil(i/m))
            if time<=h :
                ans=m
                r=m-1
            else:
                l=m+1       
            print(time,m,ans)
        return ans