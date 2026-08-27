class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1+freq.get(num,0)

        for value,count in freq.items():
            buckets[count].append(value)

        res = []

        for i in range(len(buckets)-1,0,-1):
            for item in buckets[i]:
                res.append(item)
                if len(res) >= k:
                    return res

        return res 


