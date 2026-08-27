class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        cols= defaultdict(set)
        boxes= defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                if char == ".":
                    continue
                boxid = (r//3,c//3)
                if char in rows[r] or char in cols[c] or char in boxes[boxid]:
                    return False

                rows[r].add(char)
                cols[c].add(char)
                boxes[boxid].add(char)

        return True