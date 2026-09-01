class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area,currarea = 0,0
        l,r = 0,len(heights)-1
        while l < r:
            currarea = min(heights[l],heights[r]) * (r-l)
            area = max(currarea,area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return area