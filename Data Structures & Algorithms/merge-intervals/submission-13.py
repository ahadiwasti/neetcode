class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxVal = max(interval[1] for interval in intervals)

        freq = [0]*(maxVal+1)

        res = []
        instart,inend = -1,-1

        for start,end in intervals:
            freq[start] = max(end+1,freq[start])
        
        print(freq)

        for i in range(len(freq)):
            if freq[i] != 0:
                if instart == -1:
                    instart = i
                inend = max(freq[i]-1, inend)
            if i == inend:
                res.append([instart,inend])
                instart,inend = -1,-1
        if instart != -1:
            res.append([instart,inend])

        return res


        # intervals.sort(key=lambda x:x[0])
        # res = [intervals[0]]
        # for i in range(1,len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][0] = min(intervals[i][0], res[-1][0])
        #         res[-1][1] = max(intervals[i][1], res[-1][1])
        #     else:
        #         res.append(intervals[i])
        # return res