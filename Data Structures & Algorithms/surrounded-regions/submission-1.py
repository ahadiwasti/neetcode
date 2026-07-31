class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        visited = set()
        dorections = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and (board[r][c] == "O"):
                    q.append((r,c))
                    visited.add((r,c))

        while q:
            row,col = q.popleft()
            for dr,rc in dorections:
                nr,nc = dr+row,rc+col
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or board[nr][nc] == "X":
                    continue
                
                visited.add((nr,nc))
                q.append((nr,nc))
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

            

