class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for i in range(0, len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char in t and t_char in s:
                if s_char in s_map:
                    s_map[s_char] = s_map[s_char] + 1
                else:
                    s_map[s_char] = 1
                if t_char in t_map:
                    t_map[t_char] = t_map[t_char] + 1
                else:
                    t_map[t_char] = 1
            else:
                return False
        for key in s_map:
            if s_map[key] != t_map[key]:
                return False
            
        return True