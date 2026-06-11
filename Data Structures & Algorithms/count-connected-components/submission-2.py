class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(set)
        for n1, n2 in edges:
            hmap[n1].add(n2)
            hmap[n2].add(n1)

        visited = set()

        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in hmap[node]:
                dfs(neighbor)

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res