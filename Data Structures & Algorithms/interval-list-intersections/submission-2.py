class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i=j=0

        while i < len(firstList) and j < len(secondList):
            startf,starts = firstList[i][0], secondList[j][0] 
            endf,ends = firstList[i][1], secondList[j][1]

            lo = max(startf,starts)
            hi = min(endf,ends)

            if lo <= hi:
                res.append([lo,hi])

            if endf < ends:
                i+=1
            else:
                j+=1

        return list(res)