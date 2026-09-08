class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []
        for value, count in freq.items():
            buckets[count].append(value)
        for item in range(len(buckets)-1,0,-1):
            for val in buckets[item]:
                res.append(val)
                if len(res) >= k:
                    return res
        return res

        
