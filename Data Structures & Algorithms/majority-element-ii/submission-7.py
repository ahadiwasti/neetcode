class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        for item,count in freq.items():
            if count > len(nums)//3:
                res.append(item)

        return res


        