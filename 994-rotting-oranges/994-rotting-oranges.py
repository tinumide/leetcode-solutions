from collections import deque

class Orange:
    
    def __init__(self, row, col, time):
        self.row = row
        self.col = col
        self.time = time
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        rotten_oranges = dict()
        min_time_elapsed = 0
        rows = [-1, 0, 0, 1]
        cols = [0, -1, 1, 0]
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    rotten_orange = Orange(i, j, 0)
                    rotten_oranges[(i,j)] = rotten_orange
                    queue.append(rotten_orange)
                    
        while queue:
            
            r_orange = queue.popleft()
            row = r_orange.row
            col = r_orange.col
            t = r_orange.time
            
            for i, j in zip(rows, cols):
                0, 1
                o_row = row + i
                o_col = col + j
                
                if (o_row >= 0 and o_row < len(grid)) and (o_col >= 0 and o_col < len(grid[0])) and not rotten_oranges.get((o_row, o_col)) and grid[o_row][o_col] != 0:
                    grid[o_row][o_col] = 2
                    rotten_orange = Orange(o_row, o_col, t+1)
                    rotten_oranges[(o_row,o_col)] = rotten_orange
                    queue.append(rotten_orange)
                    min_time_elapsed = max(min_time_elapsed, t+1)
                    
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    return -1
        
        return min_time_elapsed
                    
                
                
            
            
                    
        
                    
        
        
        