class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows): #add all 0 cells
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))

        def addToQ(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in seen or grid[r][c] == -1:
                return
            seen.add((r,c))
            q.append([r,c])

        #bfs we do iteratively
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                addToQ(r+1, c)
                addToQ(r-1, c)
                addToQ(r, c+1)
                addToQ(r, c-1)
            distance += 1
