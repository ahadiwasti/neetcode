class MedianFinder:
    def __init__(self):
        self.small,self.large = [],[]
    def addNum(self,num):
        if len(self.large) > 0 and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small, -1*num)

        if len(self.small) > len(self.large)+1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val*-1)

    def findMedian(self)->float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0]+(-1*self.small[0]))/2

        
        
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