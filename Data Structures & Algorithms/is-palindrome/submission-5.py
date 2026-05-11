class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        actual_i, actual_j = 0, len(s) -1
        while actual_i < actual_j:
            while actual_i < actual_j and not s[actual_i].isalnum():
                actual_i += 1
            while actual_i < actual_j and not s[actual_j].isalnum():
                actual_j -= 1
            if s[actual_i] != s[actual_j]:
                return False
            actual_i += 1
            actual_j -= 1
        return True


            