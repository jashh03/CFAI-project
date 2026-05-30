from collections import deque

grid = [
['S','0','0','X','0'],
['0','X','0','X','0'],
['0','X','0','0','0'],
['0','0','X','X','0'],
['0','0','0','0','G']
]

start = (0,0)
goal = (4,4)

rows = len(grid)
cols = len(grid[0])

directions = [(1,0),(-1,0),(0,1),(0,-1)]

queue = deque([(start,[start])])
visited = {start}

while queue:
    (x,y), path = queue.popleft()

    if (x,y) == goal:
        print("===== CO2 : BFS Search =====\n")

        print("GRID:")
        for row in grid:
            print(row)

        print("\nShortest Path Found:")
        print(path)

        print("\nPath Length =", len(path))
        print("Goal Reached Successfully")
        break

    for dx,dy in directions:
        nx,ny = x+dx,y+dy

        if 0<=nx<rows and 0<=ny<cols:
            if grid[nx][ny] != 'X' and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny),path+[(nx,ny)]))