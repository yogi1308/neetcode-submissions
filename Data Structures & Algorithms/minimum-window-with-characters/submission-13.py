class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        shortest = len(s)
        shortestStr = ""
        l, r = 0, len(t)
        while r <= len(s) + 1:
            substr = s[l : r]
            valid = True
            for char in t:
                if t.count(char) > substr.count(char):
                    valid = False
                    break
            if valid:
                l += 1
                if shortest >= len(substr):
                    shortest = len(substr)
                    shortestStr = substr
            else: r += 1
        return shortestStr
                
                
            