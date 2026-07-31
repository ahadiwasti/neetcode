class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        seen = set()
        islands = 0
        def bfs(r,c):
            dq = deque()
            dq.append((r,c))
            seen.add((r,c))

            while dq:
                row,col = dq.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc

                    if nr < 0 or nc < 0 or (nr,nc) in seen or nr >= ROWS or nc >= COLS or grid[nr][nc]=="0":
                        continue
                    dq.append((nr,nc))
                    seen.add((nr,nc))





        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    islands+=1
                    bfs(r,c)

        return islands

        