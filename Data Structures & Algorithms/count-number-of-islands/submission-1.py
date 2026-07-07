class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def bfs(r,c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                rows,cols = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+rows,dc+cols
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in seen) or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    seen.add((nr,nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands +=1
        return islands