class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """           
        def validate(x, y, digit):
            for i in range(9):
                if board[x][i] == digit or board[i][y] == digit:
                    return False
            for i in (0,1,2):
                for j in (0,1,2):
                    if board[x//3*3+i][y//3*3+j] == digit:
                        return False
            return True
                     
        def solve(count):
            if count == 81:
                return True
            x, y = count // 9, count % 9
            if board[x][y] != '.':
                return solve(count+1)
            for i in range(1, 10):
                digit = str(i)
                if validate(x, y, digit):
                    board[x][y] = digit
                    if solve(count + 1):
                        return True
                    board[x][y] = '.'
            return False
        
        solve(0)