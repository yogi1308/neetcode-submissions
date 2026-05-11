class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reversed, s_new = "", ""
        for char in s:
            if char.isalnum():
                s_new += char
                s_reversed = f"{char}{s_reversed}"
        return s_new.lower() == s_reversed.lower()