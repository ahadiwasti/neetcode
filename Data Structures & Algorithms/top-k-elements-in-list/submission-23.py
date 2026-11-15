class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num]+=1

        buckets = [[] for _ in range(len(nums)+1)]

        for key,count in freq.items():
            buckets[count].append(key)

        res = []

        for i in range(len(buckets)-1,0,-1):
            for item in buckets[i]:
                res.append(item)
            
            if len(res) >= k:
                return res
        
        return res