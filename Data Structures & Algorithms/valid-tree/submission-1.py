class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = {i:[] for i in range(n)}
        for n1,n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        visit = set()
        def dfs(node,prev):
            if node in visit:
                return False

            visit.add(node)
            for nei in nodeMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False

            return True

        return dfs(0,-1) and n == len(visit)