class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = {i: set() for i in range(1, n + 1)}
        for i in trust: table[i[0]].add(i[1])
        candidates = -1
        for i in table:
            if table[i] == set(): candidates = i
        for i in table:
            if i == candidates: continue
            if candidates not in table[i]:
                return -1
        return candidates