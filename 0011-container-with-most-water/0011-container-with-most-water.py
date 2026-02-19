class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l=0
        r=n-1
        ans_water=0

        while l<r:
            
            width=r-l
            length=min(height[l],height[r])
            curr_water=length*width
            
            # if curr_water>ans_water:
            #     ans_water=curr_water
            ans_water=max(ans_water,curr_water)
        
            if length==height[l]:
                l+=1
            elif length==height[r]:
                r-=1
                
        return (ans_water)