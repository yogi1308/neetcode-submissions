class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        for r in range(1, len(s) + 1):
            substr = s[l : r]
            count = {}
            for char in substr:
                if char in count:
                    count[char] = count[char] + 1
                else:
                    count[char] = 1
            
            max_f = max(count.values())
            if len(substr) - max_f <= k and len(substr) > longest:
                longest = len(substr)
            elif len(substr) - max_f > k:
                l += 1
        return longest