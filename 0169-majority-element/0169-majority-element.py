class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp={}
        for i in nums:
            if i in mp:
                mp[i]=mp.get(i,0)+1
            else:
                mp[i]=1

        for key,value in mp.items():
            if value>=((len(nums)//2)+1):
                return(key)
                break
        