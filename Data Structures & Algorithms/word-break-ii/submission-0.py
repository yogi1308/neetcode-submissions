class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def backtrack(idx, sentence):
            if idx == len(s):
                sentence = " ".join(sentence)
                res.append(sentence[:])
                return
            for i in range(idx, len(s) + 1):
                if s[idx: i] in wordDict:
                    sentence.append(s[idx: i])
                    backtrack(i, sentence)
                    sentence.pop()
        backtrack(0, [])
        return res
                    
