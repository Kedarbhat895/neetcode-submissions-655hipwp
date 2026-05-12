class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):

            visited[row][col] = 1

            for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:

                nrow = row + i
                ncol = col + j

                if (
                    nrow >= 0 and nrow < n and
                    ncol >= 0 and ncol < m and
                    grid[nrow][ncol] == "1" and
                    visited[nrow][ncol] == 0
                ):
                    dfs(nrow, ncol)

        n = len(grid)
        m = len(grid[0])

        num = 0

        visited = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1" and visited[i][j] == 0:

                    num += 1
                    dfs(i, j)

        return num