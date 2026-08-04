class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        res = r

        while l <= r :
            lsum = (l+r)//2

            currk = 1
            currsum = 0

            for item in nums:
                if currsum + item > lsum:
                    currk +=1
                    currsum = 0

                currsum+=item

            if currk <= k:
                res = lsum
                r = lsum -1

            else:
                l = lsum +1

        return res

