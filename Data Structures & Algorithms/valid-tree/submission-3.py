class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1: return False

        hmap = defaultdict(list)
        for node1, node2 in edges:
            hmap[node1].append(node2)
            hmap[node2].append(node1)
        visited = set()

        def dfs(start):
            if start in visited:
                return
            visited.add(start)
            for node in hmap[start]:
                dfs(node)
            return
            
            
        dfs(0)
        return len(visited) == n
