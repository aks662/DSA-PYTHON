class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=nums[0]
        l=0
        h=len(nums)-1 
        while l < h:
            mid = (l + h) // 2
            if nums[l] <= nums[h]:
                ans = min(ans, nums[l])
                break
            
            if nums[mid]>=nums[l]:
                l=mid+1
                ans=min(nums[l],ans) 
            else:
                ans=min(nums[mid],ans) 
                h=mid-1
        return (ans)
        