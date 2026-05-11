class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        max_f = 0
        for r in range(1, len(s) + 1):
            substr = s[l : r]

            max_f = max(max_f, substr.count(substr[len(substr) - 1]))
            
            if len(substr) - max_f <= k and len(substr) > longest:
                longest = len(substr)
            elif len(substr) - max_f > k:
                l += 1
        return longest