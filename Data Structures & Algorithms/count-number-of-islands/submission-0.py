class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        num_islands = 0
        for i in range(R):
            for j in range(C):
                
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands