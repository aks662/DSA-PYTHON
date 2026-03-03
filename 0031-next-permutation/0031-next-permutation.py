class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        smallest_idx=-1
        smallest_value=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                smallest_idx=i
                smallest_value=nums[i]
                break

        if smallest_idx==-1:
            nums.reverse()
            return nums
        
        for j in range(n-1, smallest_idx, -1):
            if nums[j] > nums[smallest_idx]:
                nums[j],nums[smallest_idx]=nums[smallest_idx],nums[j]   
                break
        if smallest_idx!=-1:
            nums[smallest_idx+1:] = reversed(nums[smallest_idx+1:])

            return nums
       


