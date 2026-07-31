class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pacific,atlantic = set(),set()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        pacificStart = [(r,0) for r in range(rows)]+[(0,c) for c in range(cols)]
        atlanticStart = [(rows-1,c) for c in range(cols)]+[(r,cols-1) for r in range(rows)]

        def bfs(edges, visited):
            q = deque(edges)
            for r,c in edges:
                visited.add((r,c))

            while q:
                row,col = q.popleft()
                for dr,dc in direction:
                    nr,nc = row+dr,col+dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or heights[nr][nc] < heights[row][col]:
                        continue

                    q.append((nr,nc))
                    visited.add((nr,nc))

    
        bfs(pacificStart,pacific)
        bfs(atlanticStart,atlantic)

        return list(pacific & atlantic)