class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}

        for num in nums:
            freq[num] = 1+freq.get(num,0)

        for key,count in freq.items():
            if count > len(nums)//3:
                res.append(key)

        return res