class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp.get(key,[])

        res = ""
        l,r = 0, len(values)-1

        while l <= r:
            mid = (l+r)//2

            if timestamp >= values[mid][1]:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1

        return res





        
