class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        ROWS,COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        seen=set()
        counter=0
        def bfs(r,c):
            nonlocal counter
            dq=deque()
            seen.add((r,c))
            dq.append((r,c))
            counter+=1
            while dq:
                row,col = dq.popleft()
                for dr,dc in directions:
                    nr,nc = dr+row,dc+col

                    if nr<0 or nc<0 or (nr,nc) in seen or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    
                    dq.append((nr,nc))
                    seen.add((nr,nc))
                    counter+=1

            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    counter = 0
                    bfs(r,c)
                    maxarea=max(maxarea, counter)

        return maxarea