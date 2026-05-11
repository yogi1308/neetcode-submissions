class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 1
        l, r = 0, 1
        while r < len(s) + 1:
            substr = s[l : r]
            print(substr, end="")
            if substr.count(substr[len(substr) - 1]) == 2:
                l += substr.find(substr[len(substr) - 1]) + 1
                print(" if branch", "l:", l, "r:", r)
            elif substr.count(substr[len(substr) - 1]) > 2:
                l += substr.rfind(substr[len(substr) - 1]) + 1
                print(" elif branch", "l:", l, "r:", r)
            elif len(substr) > longest:
                longest = len(substr)
                print(" else branch", "longest:", longest)
            r += 1
            print("")
        return longest