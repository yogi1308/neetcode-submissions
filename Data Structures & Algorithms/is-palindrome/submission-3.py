class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for char in s:
            if char.isalnum():
                s_new += char.lower()
        return s_new == s_new[::-1]