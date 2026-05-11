class MedianFinder:

    def __init__(self):
        self.minHeap = []  # upper half
        self.maxHeap = []  # lower half (negated)

    def addNum(self, num: int) -> None:
        # Always push to maxHeap first, then rebalance to minHeap
        heapq.heappush(self.maxHeap, -num)
        
        # Enforce invariant: max of lower half <= min of upper half
        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        # Balance sizes: minHeap can have at most 1 more than maxHeap
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]