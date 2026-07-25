class Solution:
    def topKFrequent(self,nums:[int],k:int)->List[int]:
        freq= {}
        for n in nums:
            freq[n] = 1+freq.get(n,0)

        sortedItems = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        res = [key for key, count in sortedItems[:k]]

        return res