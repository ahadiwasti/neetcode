class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num]=1+counts.get(num,0)
        for num,cnt in counts.items():
            bucket[cnt].append(num)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res