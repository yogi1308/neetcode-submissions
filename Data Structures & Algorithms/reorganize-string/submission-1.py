class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        seen = set()
        for character in s:
            if character not in seen:
                times = s.count(character) * -1
                heapq.heappush(heap, [times, character])
                seen.add(character)
        string = ""
        print(heap)
        while heap:
            popped = []
            letter = []
            while heap:
                letter = heapq.heappop(heap)
                popped.append(letter)
                if not string or letter[1] != string[-1]: break
            if not string or letter[1] != string[-1]: 
                string += letter[1]
                toPush = popped.pop()
                toPush = [toPush[0] + 1, toPush[1]]
                print(string, heap)
                if toPush[0] != 0:
                    heapq.heappush(heap, toPush)
                while popped:
                    toPush = popped.pop()
                    heapq.heappush(heap, toPush)

        return "" if len(string) != len(s) else string
            