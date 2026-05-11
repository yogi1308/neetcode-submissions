class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        shortest = len(s)
        shortestStr = ""
        tmap = {}
        smap = {}
        for i in range(26):
            tmap[chr(65 + i)] = 0
            smap[chr(65 + i)] = 0
            tmap[chr(97 + i)] = 0
            smap[chr(97 + i)] = 0

        for char in t:
            tmap[char] = tmap.get(char) + 1

        for l in range(len(s) - len(t) + 1):
            matches = 0
            smap = {key: 0 for key in smap}
            for char in s[l : len(t) + l]:
                smap[char] = smap.get(char) + 1
            for char in tmap.keys():
                if tmap[char] <= smap[char]:
                    matches += 1

            for r in range(len(t) + l, len(s) + 1):
                substr = s[l : r]
                print(substr, matches)

                if r != len(t) + l:
                    smap[substr[-1]] = smap[substr[-1]] + 1
                    if smap[substr[-1]] == tmap[substr[-1]]: 
                        matches += 1
                
                if matches == 52 and len(substr) <= shortest:
                    shortest = len(substr)
                    shortestStr = substr
                    print("shortestStr:", shortestStr, "shortest:", shortest)
                    if shortest == len(t):
                        return shortestStr

        return shortestStr
