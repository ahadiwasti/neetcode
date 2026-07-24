class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nset1 = set(nums1)
        nset2 = set(nums2)
        res = []

        for n in nset1:
            if n in nset2:
                res.append(n)

        return res 