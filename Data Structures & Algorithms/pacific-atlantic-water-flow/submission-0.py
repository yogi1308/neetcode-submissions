from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        
        # Get your dimensions clearly defined
        ROWS = len(heights)
        COLS = len(heights[0])

        # 1. FIX INITIALIZATION: (col, row) to match your heights[y][x] indexing
        # Top and Bottom borders
        for x in range(COLS):
            pacific.add((x, 0))          # x varies, y is 0 (Top row)
            atlantic.add((x, ROWS - 1))  # x varies, y is ROWS-1 (Bottom row)
            
        # Left and Right borders
        for y in range(ROWS):
            pacific.add((0, y))          # x is 0, y varies (Left col)
            atlantic.add((COLS - 1, y))  # x is COLS-1, y varies (Right col)
        
        def dfs(x, y, ocean):
            # 2. ADD BOUNDARY CHECKS: Ensure neighbor stays inside the grid
            # Left
            if x - 1 >= 0 and heights[y][x - 1] >= heights[y][x]:
                if ocean == "p" and (x - 1, y) not in pacific: 
                    pacific.add((x - 1, y))
                    dfs(x - 1, y, "p")
                elif ocean == "a" and (x - 1, y) not in atlantic: 
                    atlantic.add((x - 1, y))
                    dfs(x - 1, y, "a")
            # Right
            if x + 1 < COLS and heights[y][x + 1] >= heights[y][x]:
                if ocean == "p" and (x + 1, y) not in pacific: 
                    pacific.add((x + 1, y))
                    dfs(x + 1, y, "p")
                elif ocean == "a" and (x + 1, y) not in atlantic: 
                    atlantic.add((x + 1, y))
                    dfs(x + 1, y, "a")
            # Up
            if y - 1 >= 0 and heights[y - 1][x] >= heights[y][x]:
                if ocean == "p" and (x, y - 1) not in pacific: 
                    pacific.add((x, y - 1))
                    dfs(x, y - 1, "p")
                elif ocean == "a" and (x, y - 1) not in atlantic: 
                    atlantic.add((x, y - 1))
                    dfs(x, y - 1, "a")
            # Down
            if y + 1 < ROWS and heights[y + 1][x] >= heights[y][x]:
                if ocean == "p" and (x, y + 1) not in pacific: 
                    pacific.add((x, y + 1))
                    dfs(x, y + 1, "p")
                elif ocean == "a" and (x, y + 1) not in atlantic: 
                    atlantic.add((x, y + 1))
                    dfs(x, y + 1, "a")

        # 3. FIX ITERATION: Convert to list copies so sets can safely grow inside DFS
        for x, y in list(pacific): dfs(x, y, "p")
        for x, y in list(atlantic): dfs(x, y, "a")

        # 4. FIX OUTPUT FORMAT: Return [y, x] (row, col) as expected by LeetCode
        common = []
        for (x, y) in pacific:
            if (x, y) in atlantic: 
                common.append([y, x]) # heights[y][x] means y is row, x is col

        return common