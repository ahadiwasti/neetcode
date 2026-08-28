class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1+freq.get(num,0)

        for value,count in freq.items():
            bucket[count].append(value)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for item in bucket[i]:
                res.append(item)
                if len(res) >= k:
                    return res
        return res