class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """           
        def validate(i, j, digit):
            for a in range(9):
                if board[i][a] == digit or board[a][j] == digit:
                    return False
            
            for x in (0,1,2):
                for y in (0,1,2):
                    if board[i-i%3+x][j-j%3+y] == digit:
                        return False 
            return True
            
        def solve(count):
            if count == 81:
                return True
            i, j = count//9, count%9
            if board[i][j] != '.':
                return solve(count+1)
            
            for k in range(1, 10):
                digit = str(k)
                if validate(i, j, digit):
                    board[i][j] = digit
                    if solve(count+1):
                        return True
                    board[i][j] = '.'
            return False
            
        solve(0)