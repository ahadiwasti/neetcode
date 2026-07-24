class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set(nums1)
        resSet = set()
        res = []
        for n in nums2:
            if n in numSet:
                resSet.add(n)
        for item in resSet:
            res.append(item)
        return res