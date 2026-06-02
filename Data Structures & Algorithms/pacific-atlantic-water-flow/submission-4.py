class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        for x in range(len(heights[0])):
            pacific.add((0, x))                      # top row
            atlantic.add((len(heights) - 1, x))      # bottom row
        for y in range(len(heights)):
            pacific.add((y, 0))                      # left col
            atlantic.add((y, len(heights[0]) - 1))   # right col
        
        def dfs(y, x, ocean):
            visited = pacific if ocean == "p" else atlantic
            if x - 1 >= 0 and heights[y][x - 1] >= heights[y][x] and (y, x - 1) not in visited:
                visited.add((y, x - 1))
                dfs(y, x - 1, ocean)
            if x + 1 < len(heights[0]) and heights[y][x + 1] >= heights[y][x] and (y, x + 1) not in visited:
                visited.add((y, x + 1))
                dfs(y, x + 1, ocean)
            if y - 1 >= 0 and heights[y - 1][x] >= heights[y][x] and (y - 1, x) not in visited:
                visited.add((y - 1, x))
                dfs(y - 1, x, ocean)
            if y + 1 < len(heights) and heights[y + 1][x] >= heights[y][x] and (y + 1, x) not in visited:
                visited.add((y + 1, x))
                dfs(y + 1, x, ocean)

        for y, x in pacific.copy(): dfs(y, x, "p")
        for y, x in atlantic.copy(): dfs(y, x, "a")

        return [[y, x] for (y, x) in pacific if (y, x) in atlantic]