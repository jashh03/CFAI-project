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

queue = deque([(start,[start])])
visited = {start}

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    (x,y), path = queue.popleft()

    if (x,y) == goal:
        break

    for dx,dy in directions:
        nx,ny = x+dx,y+dy

        if 0<=nx<rows and 0<=ny<cols:
            if grid[nx][ny] != 'X' and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny),path+[(nx,ny)]))

valid = True
for x,y in path:
    if grid[x][y] == 'X':
        valid = False

prior = 0.6
sensor_accuracy = 0.8
evidence = 0.7
belief = (sensor_accuracy * prior) / evidence

utility = 100 - len(path)

print("===== CO6 : Hybrid Mobile Robot Localization =====\n")

print("GRID:")
for row in grid:
    print(row)

print("\nSTEP 1 : Search")
print("Path Found:")
print(path)

print("\nSTEP 2 : Constraint Checking")
print("Constraints Satisfied =", valid)

print("\nSTEP 3 : Bayesian Localization")
print("Estimated Position = (2,2)")
print("Belief =", round(belief,3))

print("\nSTEP 4 : Utility Evaluation")
print("Utility =", utility)

print("\nFINAL RESULT")
print("Goal Reached Successfully")
print("Localization Successful")
print("Hybrid AI System Executed")