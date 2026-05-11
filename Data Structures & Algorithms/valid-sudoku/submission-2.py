class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for i in range(0, 9):
            col = set()
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in col:
                    return False
                col.add(board[j][i])

            print(col)

        start_row = 0
        start_col = 0

        for y in range(3):
            for x in range(3):
                cell = set()
                for i in range(3):
                    for j in range(3):
                        if board[start_row + i][start_col + j] == ".":
                            continue
                        elif board[start_row + i][start_col + j] in cell:
                            return False
                        cell.add(board[start_row + i][start_col + j])

                start_row += 3
            start_col += 3
            start_row = 0

        return True

                
        