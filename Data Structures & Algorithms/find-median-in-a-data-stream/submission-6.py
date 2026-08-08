class MedianFinder:
    def __init__(self):
        self.minh, self.maxh = [],[]

    def addNum(self,num):
        if len(self.maxh) > 0 and num > self.maxh[0]:
            heapq.heappush(self.maxh,num)

        else:
            heapq.heappush(self.minh,-1*num)

        if len(self.minh) > len(self.maxh):
            val = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -1*val)

        if len(self.maxh) > len(self.minh):
            val = heapq.heappop(self.maxh)
            heapq.heappush(self.minh,-1*val)

    def findMedian(self):
        if len(self.minh) > len(self.maxh):
            return -1*self.minh[0]
        elif len(self.maxh) > len(self.minh):
            return self.maxh[0]
        else:
            return ((-1*self.minh[0])+self.maxh[0])/2

        
        
        # this one important not listed in neetcode

#         class StockPrice:

#     def __init__(self):
#         self.createdat = {}
#         self.maxp = []
#         self.minp = []
#         self.updatedat = 0
        

#     def update(self, timestamp: int, price: int) -> None:
#         self.createdat[timestamp] = price
#         self.updatedat = max(self.updatedat,timestamp)
#         heapq.heappush(self.maxp,(price,timestamp))
#         heapq.heappush(self.minp,(-1*price,timestamp))

#     def current(self) -> int:
#         return self.createdat[self.updatedat]
        

#     def maximum(self) -> int:
#         while True:
#             price , ts = self.minp[0]
#             if -price == self.createdat[ts]:
#                 return -price

#             heapq.heappop(self.minp)
        

#     def minimum(self) -> int:
#         while True:
#             price,ts = self.maxp[0]
#             if price == self.createdat[ts]:
#                 return price

#             heapq.heappop(self.maxp)
        


# # Your StockPrice object will be instantiated and called as such:
# # obj = StockPrice()
# # obj.update(timestamp,price)
# # param_2 = obj.current()
# # param_3 = obj.maximum()
# param_4 = obj.minimum()