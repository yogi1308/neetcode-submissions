class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        done_char = set()
        for i in range(0, len(s)):
            s_count = 0
            t_count = 0
            char = s[i]
            if char not in done_char:
                done_char.add(char)
                for c in s:
                    if c == char:
                        s_count += 1
                for c in t:
                    if c == char:
                        t_count += 1
                if s_count != t_count:
                    return False
        return True