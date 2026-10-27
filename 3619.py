class Solution:
    from collections import deque
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        def bfs(x,y):
            if grid[x][y] == 0:
                return 0
            count = grid[x][y]
            vectors = [(0,1),(1,0),(0,-1),(-1,0)]
            todo = deque([(x,y)])
            grid[x][y] = 0
            while True:
                if len(todo) == 0:
                    break
                a,b = todo.popleft()
                for dx, dy in vectors:
                    nx, ny = a+dx, b+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                        count += grid[nx][ny]
                        todo.append((nx,ny))
                        grid[nx][ny] = 0
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c = bfs(i,j)
                if c > 0 and c%k == 0:
                    ans += 1
        return ans