class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                add=nums[i] + nums[j] + nums[k]
                if add>0:
                    k-=1
                elif add<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res

                
            






        # nums.sort()
        # n=len(nums)
        # res=[]
        # for i in range(n):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     for j in range(i+1,n):
        #         if j>i+1 and nums[j]==nums[j-1]:
        #             continue
        #         for k in range(j+1, n):
        #             if k>j+1 and nums[k]==nums[k-1]:
        #                 continue
        #             sum=nums[i] + nums[j] + nums[k]
        #             if sum==0:
        #                 res.append([nums[i], nums[j],nums[k]])
        # return res
                
            

        
       

        