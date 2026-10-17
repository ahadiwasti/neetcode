class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxval = max(interval[1] for interval in intervals)
        mp = [0]*(maxval+1)

        res = []

        for mstart, mend in intervals:
            mp[mstart] = max(mp[mstart], mend+1)
        start = end = -1
        for i in range(maxval+1):
            if mp[i] != 0:
                if start == -1:
                    start = i
                end = max(mp[i]-1, end)

            if end == i:
                res.append([start, end])
                start = end = -1

        if start != -1:
            res.append([start, end])

        return res
