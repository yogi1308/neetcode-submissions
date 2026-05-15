class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(substrings, idx):
            if len("".join(substrings)) == len(s):
                res.append(substrings[:])
            for end in range(idx, len(s)):
                string = s[idx:end + 1]
                if string == string[::-1]:
                    substrings.append(s[idx:end + 1])
                    dfs(substrings, end + 1)
                    substrings.pop()
        dfs([], 0)
        return res