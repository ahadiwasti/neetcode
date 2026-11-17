class Solution:
    def longestConsecutive(self, nums:List[int])-> int:
        seen = set(nums)
        curr = 0
        resp = float('-inf')
        if not nums:
            return 0
        for num in nums:
            if num-1 not in seen:
                curr = 1
                while num+curr in seen:
                    curr+=1

            resp = max(curr,resp)
        return resp 