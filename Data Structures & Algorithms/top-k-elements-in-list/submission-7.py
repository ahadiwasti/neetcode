class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n] = 1+freq.get(n,0)

        for key, value in freq.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for count in bucket[i]:
                res.append(count)
                if len(res) == k:
                    return res
        return res        
