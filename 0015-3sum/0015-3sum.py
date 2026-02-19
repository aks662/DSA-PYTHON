class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''hashing'''
        ans=set()
        nums=sorted(nums)
        n=len(nums)

        for i in range(0,n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            seen=set()
            for j in range(i+1,n):
                
                # if j>i+1 and  nums[j]==nums[j-1]:
                #     continue
                
                k=-(nums[i]+nums[j])
                
                if k in seen:
                    ans.add((nums[i],k,nums[j]))
                            
                else:
                    seen.add(nums[j])
        return ([list(t) for t in ans])




        '''2_pointers'''
        # nums=sorted(nums)
        # ans=[]
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]>0:
        #         break
        #     if i>0 and nums[i]==nums[i-1]: 
        #         continue
            
        #     target=-(nums[i])
        #     l=i+1
        #     r=n-1

        #     while l<r:
                    
        #         curr_sum=nums[l]+nums[r]
                
        #         if curr_sum==target:
                    
        #             ans.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1   
        #             while l<r and nums[l]==nums[l-1]:
        #                 l+=1
        #             while r>l and nums[r]==nums[r+1]:
        #                 r-=1
                        
        #         elif curr_sum<target:
        #             l+=1
        #         else:
        #             r-=1
                        
                    
                    
                    
        # return (ans)
        