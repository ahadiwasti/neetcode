class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        mp = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            mp[num] = 1+mp.get(num,0)

        for value,count in mp.items():
            buckets[count].append(value)

        res = []
        for item in range(len(buckets)-1,0,-1):
            for n in buckets[item]:
                res.append(n)

            if len(res) >= k:
                return res

        return res

