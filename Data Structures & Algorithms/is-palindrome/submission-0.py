class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s_reversed = list(s)
        s_reversed = s_reversed[::-1]
        print(s_reversed)
        s_reversed = "".join(s_reversed)
        print(s, s_reversed)
        return s.lower() == s_reversed.lower()