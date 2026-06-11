class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = {}
        for n1, n2 in edges:
            hmap.setdefault(n1, set()).add(n2)
            hmap.setdefault(n2, set()).add(n1)
        print(hmap)
        visited = set()
        def dfs(node, visitedNow):
            if node in visitedNow: return
            visitedNow.add(node)
            if node in visited:
                return True
            visited.add(node)
            for n in hmap[node]:
                if dfs(n, visitedNow): return True
            return False
        
        res = 0
        for node in hmap:
            if not dfs(node, set()): res += 1

        if len(visited) < n:
            for i in range(n - len(visited)):
                res += 1
                
        return res
