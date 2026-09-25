class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        n=len(nums)-1
        r=n
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            #check left sorted array:
            if nums[l]<=nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l=mid+1 #move right
                else:
                    r=mid-1
            #check right sorted array:
            else:
                if target > nums[r]or target < nums[mid]:
                    r=mid-1 #move left
                else:
                    l=mid+1
        return -1











        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1
