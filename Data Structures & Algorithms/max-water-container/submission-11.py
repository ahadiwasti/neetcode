class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currarea = area = 0
        l,r = 0, len(heights)-1
        while l < r:
            currarea = min(heights[l],heights[r])*(r-l)
            area = max(area,currarea)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return area

# T:O(n)
# S:O(1)
