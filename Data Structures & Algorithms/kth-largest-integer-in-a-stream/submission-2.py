import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        print(self.heap, nums, self.k)

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[self.k - 1]
