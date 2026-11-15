class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []

        for key,count in counts.items():
            if count > len(nums)/3:
                res.append(key)

        return res
