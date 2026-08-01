class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        mp = {i:[] for i in range(n)}
        visited = set()

        for n1,n2 in edges:
            mp[n1].append(n2)
            mp[n2].append(n1)
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for nei in mp[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and n == len(visited)

