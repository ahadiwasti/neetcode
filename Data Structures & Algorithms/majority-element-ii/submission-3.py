class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1+ freq.get(num,0)

        res = []
        for value,count in freq.items():
            if count > (len(nums)//3):
                res.append(value)

        return res