class Solution:
    def dfs(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.dfs(x + 1, y, grid)
        self.dfs(x - 1, y, grid)
        self.dfs(x, y + 1, grid)
        self.dfs(x, y - 1, grid)

        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    count += 1
                    grid = self.dfs(x, y, grid)
        return count
