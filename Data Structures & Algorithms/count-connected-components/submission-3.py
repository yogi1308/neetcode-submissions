class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(set)
        for n1, n2 in edges:
            hmap.setdefault(n1, set()).add(n2)
            hmap.setdefault(n2, set()).add(n1)

        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for n in hmap[node]:
                dfs(n)
        
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res
