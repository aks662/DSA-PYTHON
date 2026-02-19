class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''hashing'''
        # curr_sum=[]
        # nums=sorted(nums)
        # n=len(nums)

        # for i in range(0,n):
        #     if nums[i]>0:
        #         break
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
            
        #     seen=set()
        #     for j in range(i+1,n):
        #         if nums[j]==nums[j-1]:
        #             continue
        #         k=-(nums[i]+nums[j])
        #         if k in seen:
        #             curr_sum.append([nums[i],k,nums[j]])
                    
        #             while j + 1 < n and nums[j] == nums[j+1]: #checking for duplicated for value of k and skipping them
        # 
        #                     j += 1
                            
        #         else:
        #             seen.add(nums[j])
        # print(curr_sum)



        '''2_pointers'''
        nums=sorted(nums)
        ans=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]: 
                continue
            
            target=-(nums[i])
            l=i+1
            r=n-1

            while l<r:
                    
                curr_sum=nums[l]+nums[r]
                
                if curr_sum==target:
                    
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1   
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                        
                elif curr_sum<target:
                    l+=1
                else:
                    r-=1
                        
                    
                    
                    
        return (ans)
        