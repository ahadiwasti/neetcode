class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        room = 0

        dq= deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r,c))
    
        counter = 0
        while dq:
            counter+=1 
            for _ in range(len(dq)):
                row,col = dq.popleft()   
                visited.add((row,col)) 
                for dr,dc in direction:
                    nr,nc = row+dr,col+dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue

                    dq.append((nr,nc))
                    visited.add((nr,nc))
                    grid[nr][nc] = counter



