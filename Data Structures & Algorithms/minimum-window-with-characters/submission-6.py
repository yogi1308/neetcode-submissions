class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        shortest = len(s)
        shortestStr = ""
        tmap = {}
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1

        for l in range(len(s) - len(t) + 1):
            for r in range(len(t) + l, len(s) + 1):
                substr = s[l : r]
                valid = True

                for char in tmap.keys():
                    if tmap[char] > substr.count(char):
                        valid = False
                        break
                if valid and len(substr) <= shortest:
                    shortest = len(substr)
                    shortestStr = substr
        return shortestStr
