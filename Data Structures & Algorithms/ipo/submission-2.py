class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        for i in range(len(profits)):
            heapq.heappush(heap, (profits[i] * -1, capital[i]))
        for i in range(k):
            popped = [] 
            popped_element = (0, 0)
            while heap:
                popped_element = heapq.heappop(heap)
                if popped_element[1] <= w: break
                popped.append(popped_element)
                popped_element = (0, 0)
            w += popped_element[0] * -1
            print(popped_element, popped)
            for p in popped:
                heapq.heappush(heap, p)
        return w
