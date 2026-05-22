class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []

        # def addWord(word):
        #     curr = root
        #     for c in word:
        #         if c not in curr.children:
        #             curr.children[c] = TrieNode()
        #         curr = curr.children[c]
        #     curr.end = True

        # for word in words:
        #     addWord(word)

        def dfs(x, y, occupied, word):
            if board[y][x] != word[0]: return False
            if (x, y) in occupied: return False
            if len(word) == 1: return True
            flag = False
            occupied.append((x, y))
            if x - 1 >= 0:
                if dfs(x - 1, y, occupied, word[1:]): flag = True
            if x + 1 < len(board[0]):
                if dfs(x + 1, y, occupied, word[1:]): flag = True
            if y - 1 >= 0:
                if dfs(x, y - 1, occupied, word[1:]): flag = True
            if y + 1 < len(board):
                if dfs(x, y + 1, occupied, word[1:]): flag = True

            return flag
        
        for word in words:
            flag = False
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if dfs(x, y, [], word): 
                        res.append(word)
                        flag = True
                        break
                if flag: break

        return res


