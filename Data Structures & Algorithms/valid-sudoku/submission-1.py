class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for i in range(1, 10):
                if row.count(str(i)) > 1:
                    return False

        for i in range(0, 9):
            col = []
            for j in range(0, 9):
                col.append(board[j][i])

            print(col)

            for k in range(1, 10):
                if col.count(str(k)) > 1:
                    return False

        start_row = 0
        start_col = 0

        for y in range(3):
            for x in range(3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        cell.append(board[start_row + i][start_col + j])
                
                for k in range(1, 10):
                    if cell.count(str(k)) > 1:
                        return False

                start_row += 3
            start_col += 3
            start_row = 0

        return True

                
        