class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = {i:[] for i in range(n)}

        for n1,n2 in edges:
            mp[n1].append(n2)
            mp[n2].append(n1)

        visited = set()
        counted = 0
        def dfs(node):
            visited.add(node)
            for nei in mp[node]:
                if nei in visited:
                    continue
                dfs(nei)

        for i in range(n):
            if i not in visited:
                counted+=1
                dfs(i)

        return counted