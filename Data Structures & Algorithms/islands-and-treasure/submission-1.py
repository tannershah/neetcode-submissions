from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #bfs with treasure chests as sources
        #upon discovery, grid[i][j] = value(parent) + 1
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            row, col = q.popleft()

            neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

            def in_bounds(r,c):
                return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])
            
            for r,c in neighbors:
                if not in_bounds(r,c) or grid[r][c] < 2147483647:
                    continue 
                grid[r][c] = grid[row][col] + 1
                q.append((r,c))
            
