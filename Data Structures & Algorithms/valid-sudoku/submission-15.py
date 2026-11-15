class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols= defaultdict(set)
        boxes= defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                boxid = (r//3,c//3)

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[boxid]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[boxid].add(board[r][c])

        return True