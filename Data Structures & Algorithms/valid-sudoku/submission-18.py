class Solution:
    def isValidSudoku(self, matrix) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                char = matrix[r][c]
                if char == ".":
                    continue

                boxid = (r//3, c//3)

                if char in rows[r] or char in cols[c] or char in boxes[boxid]:
                    return False

                rows[r].add(char)
                cols[c].add(char)
                boxes[boxid].add(char)

        return True