class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(x, y):
            q = [(x, y)]
            grid[x][y] = 1
            while q:
                i, j = q.pop()
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        q.append((ni, nj))

        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 0: bfs(i, j)
        for j in range(n):
            for i in (0, m - 1):
                if grid[i][j] == 0: bfs(i, j)

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    bfs(i, j)
                    ans += 1
        return ans