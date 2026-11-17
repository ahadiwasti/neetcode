class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        resp = []
        for key,count in counts.items():
            if count > len(nums)//3:
                resp.append(key)

        return resp