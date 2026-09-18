class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        n=len(heights)
        left=0
        right=n-1
        while left<right:
            height= min(heights[left],heights[right])
            width= right-left
            area=width*height
            max_area=max(max_area,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_area
        








        # max_area=0
        # n=len(heights)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         width=j-i
        #         height=min(heights[i],heights[j])
        #         area= width*height
        #     max_area=max(max_area,area)
        # return max_area
        