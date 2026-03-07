class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        w1=None
        w2=None
        c1=0
        c2=0
        for n in nums:
            if w1==n:
                c1+=1
            elif w2==n:
                c2+=1
            elif c1==0:
                w1=n
                c1=1
            elif c2==0:
                w2=n
                c2=1
            else:
                c1-=1
                c2-=1
                
        count_w1=nums.count(w1)
        count_w2=nums.count(w2)

        ans=[]
        if count_w1>(len(nums)//3):

            ans.append(w1)
        if count_w2>(len(nums)//3) and w1!=w2:

            ans.append(w2)
        return(ans)