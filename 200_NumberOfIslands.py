class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       

        def bfs(i, j):
            q = deque([(i,j)])
            grid[i][j] = 'l'
            
            while q:
                a, b = q.popleft()
                for shiftx, shifty in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x = a + shiftx
                    y = b + shifty
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':
                        continue
                    grid[x][y] = 'l'
                    q.append((x, y))
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count
                    
                    
                    
                    
                    