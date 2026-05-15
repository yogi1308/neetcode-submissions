class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(substrings, idx, length):
            if length == len(s):
                res.append(substrings[:])
            for end in range(idx, len(s)):
                string = s[idx:end + 1]
                if string == string[::-1]:
                    substrings.append(string)
                    dfs(substrings, end + 1, length + len(string))
                    substrings.pop()
        dfs([], 0, 0)
        return res