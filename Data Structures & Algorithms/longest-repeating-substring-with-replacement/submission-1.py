class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        count = {}
        for l in range(len(s)):
            for r in range(l + 1, len(s) + 1):
                substr = s[l : r]
                for char in substr:
                    if char in count:
                        count[char] = count[char] + 1
                    else:
                        count[char] = 1
                
                max_f = max(count.values())
                if len(substr) - max_f <= k and len(substr) > longest:
                    longest = len(substr)
                count.clear()
        return longest
                
