class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]: return False
                l += 1; r -= 1
            return True

        def dfs(substrings, idx, length):
            if length == len(s):
                res.append(substrings[:])
            for end in range(idx, len(s)):
                string = s[idx:end + 1]
                if is_palindrome(string):
                    substrings.append(string)
                    dfs(substrings, end + 1, length + len(string))
                    substrings.pop()
        dfs([], 0, 0)
        return res