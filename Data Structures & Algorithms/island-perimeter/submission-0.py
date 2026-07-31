class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        ROWS,COLS = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        if nr < 0 or nc < 0 or nr >=ROWS or nc >= COLS:
                            perimeter+=1
                            continue
                        
                        if grid[nr][nc] == 1:
                            continue
                        
                        perimeter+=1
    
        return perimeter

