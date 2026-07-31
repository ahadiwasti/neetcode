class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        pacific = set()
        atlantic = set()
        res = []
      
        def bfs(starts, visited):
            dq=deque(starts)


            for r, c in starts:
                visited.add((r,c))
            
            while dq:
                rows,cols = dq.popleft()
                for dr,dc in directions:
                    nr,nc = rows+dr,cols+dc

                    if nr < 0 or nc < 0 or nr>=ROWS or nc >= COLS or (nr,nc) in visited or heights[nr][nc] < heights[rows][cols]:
                        continue

                    visited.add((nr,nc))
                    dq.append((nr,nc))

        pacificStarts = [(0,c) for c in range(COLS)]+[(r,0) for r in range(ROWS)]
        atlanticStarts = [(ROWS-1,c) for c in range(COLS)]+[(r,COLS-1) for r in range(ROWS) ]

        bfs(pacificStarts,pacific)
        bfs(atlanticStarts,atlantic)

        return list(pacific & atlantic)