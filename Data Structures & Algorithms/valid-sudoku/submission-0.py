class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use a hashset for each row, col, and sub-box
        # checking rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])

        # checking columns
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])

        # checking sub-boxes
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col]) 

        return True
        
        

        