class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        l_max=[0]*n
        l_max[0]=height[0]
        for i in range(1,n):
            l_max[i]=max(height[i],l_max[i-1])
            
            
        r_max=[0]*n
        r_max[-1]=height[-1]
        for i in range(n-2,-1,-1):
            r_max[i]=max(height[i],r_max[i+1])

        # water=0
        store_water=0
        for i in range(n):
            if min(l_max[i],r_max[i])-height[i]>0:
                store_water+=min(l_max[i],r_max[i])-height[i]
                
            '''for max water trap''' 
            
            # if i>0 and l_max[i]!=l_max[i-1]:
            #     store_water=0
            # water=max(water,store_water)
            
        return (store_water)