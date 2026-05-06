class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
            if grid is None:
                return None
            ROWS = len(grid)
            COLS = len(grid[0])
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            def isValid(row, col):
                return 0<= row < ROWS and 0<=col<COLS and grid[row][col] != -1
            queue = deque()
            INF = 2147483647
            visited = set()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == INF:
                        queue.append((r, c, 0))
                        visited.add((r,c))
                        while queue:
                            for _ in range(len(queue)):
                                row, col, steps = queue.popleft()
                                if grid[row][col] == 0:
                                    grid[r][c] = steps
                                    visited.clear()
                                    queue.clear()
                                    break
                                for (dr,dc) in directions:
                                    nextRow = row+dr
                                    nextCol = col+dc
                                    if (isValid(nextRow, nextCol) and (nextRow, nextCol) not in visited):
                                        queue.append((nextRow, nextCol, steps+1))
                                        visited.add((nextRow, nextCol))      
            return 
