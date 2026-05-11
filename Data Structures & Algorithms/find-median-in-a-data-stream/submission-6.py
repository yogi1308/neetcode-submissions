import heapq

class MedianFinder:
    def __init__(self):
        # maxHeap stores the smaller half (using negative values for Python's min-heap)
        self.small = [] 
        # minHeap stores the larger half
        self.large = [] 

    def addNum(self, num: int) -> None:
        # 1. Add to max-heap (small half), then move the largest of those to min-heap
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 2. Rebalance: large half should never have more than 1 extra element
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0