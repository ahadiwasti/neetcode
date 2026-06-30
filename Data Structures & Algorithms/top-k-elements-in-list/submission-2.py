class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        counts = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num]=1+counts.get(num,0)
        for key,value in counts.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for item in bucket[i]:
                res.append(item)
                if len(res)==k:
                    return res