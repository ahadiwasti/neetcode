class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for item,count in freq.items():
            if count > len(nums)//3:
                res.append(item)

        return res
