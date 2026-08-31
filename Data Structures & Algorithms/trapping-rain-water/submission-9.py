class Solution:
    def trap(self, heights: list[int]) -> int:
        leftmax,rightmax = 0,0
        res = 0
        l,r = 0, len(heights)-1

        while l < r:
            leftmax = max(leftmax,heights[l])
            rightmax = max(rightmax,heights[r])

            if leftmax < rightmax:
                res += leftmax - heights[l]
                l+=1
            else:
                res += rightmax - heights[r]
                r-=1

        return res