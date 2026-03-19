class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0 :
            # print(nums1)
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                # print(i,"i")
                i-=1
                
            else:
                nums1[k]=nums2[j]
                # print(j,"j")
                j-=1

            k-=1
        # print(i,j)      
        if j>=0:
            for j in range(j,-1,-1):
                nums1[j]=nums2[j]
        # print(nums1)  