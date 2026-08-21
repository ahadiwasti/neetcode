class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            freq[nums[i]] = 1+ freq.get(nums[i],0)

        for key,value in freq.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for value in buckets[i]:
                res.append(value)
                if len(res) >= k:
                    return res

        return res

