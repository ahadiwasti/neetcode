class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = set()
        minutes=fresh = 0
        dq = deque()
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

       

        while dq and fresh >0 :
            for i in range(len(dq)):
                row,col = dq.popleft()

                for dr,dc in directions:
                    nr,nc = row+dr , col+dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or grid[nr][nc] !=1:
                        continue
                    visited.add((nr,nc))
                    dq.append((nr,nc))
                    fresh -=1
            minutes+=1
                    

        return minutes if fresh == 0 else -1

        