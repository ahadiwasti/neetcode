class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        for key,count in freq.items():
            buckets[count].append(key)

        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                res.append(val)
                if len(res) >= k :
                    return res

        return res