class Solution:
    def totalNQueens(self, n: int) -> int:

        def placeQueen(i, k):
            cols.append(i)
            diags.append(i+k)
            offdiags.append(i-k)
            queens.append([k, i])
            
        def takeQueen(i, k):
            cols.remove(i)
            diags.remove(i+k)
            offdiags.remove(i-k)
            queens.remove([k, i])
            
        def solve(k): #kth queen
            for i in range(n):
                if i not in cols and i+k not in diags and i-k not in offdiags and [i,k] not in queens:
                    placeQueen(i,k)
                    if k == n-1:
                        res.append('Q')
                    else:
                        solve(k+1)
                    takeQueen(i, k)
                
        res = []
        cols = []
        diags = []
        offdiags = []
        queens = []
        solve(0)
        return len(res)