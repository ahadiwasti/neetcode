class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = water = 0

        l,r= 0,len(heights)-1

        while l < r:
            area = min(heights[l],heights[r])*(r-l)
            water = max(area,water)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return water
# T:O(n)
# S:O(1)
