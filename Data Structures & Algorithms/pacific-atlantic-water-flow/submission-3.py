class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for col in range(cols):
            pacific.add((0, col))       # top row
            atlantic.add((rows - 1, col))  # bottom row
        for row in range(rows):
            pacific.add((row, 0))       # left col
            atlantic.add((row, cols - 1))  # right col

        def dfs(row, col, visited):
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and heights[r][c] >= heights[row][col]:
                    visited.add((r, c))
                    dfs(r, c, visited)

        for row, col in pacific.copy(): dfs(row, col, pacific)
        for row, col in atlantic.copy(): dfs(row, col, atlantic)

        return [[r, c] for r, c in pacific if (r, c) in atlantic]