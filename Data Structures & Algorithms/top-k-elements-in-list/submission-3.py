class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        counts = {}
        bucket = [[] for i in range(len(nums)+1)]

        for n in nums:
            counts[n] = 1+counts.get(n,0)
        for key,value in counts.items():
            bucket[value].append(key)
        res = []
        for item in range(len(bucket)-1,0,-1):
            for num in bucket[item]:
                res.append(num)
                if len(res) == k:
                    return res 

                