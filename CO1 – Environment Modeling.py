from dataclasses import dataclass

grid = [
['S','0','0','X','0'],
['0','X','0','X','0'],
['0','X','0','0','0'],
['0','0','X','X','0'],
['0','0','0','0','G']
]

@dataclass
class State:
    x: int
    y: int

start = State(0,0)
goal = State(4,4)

print("===== CO1 : Environment Modeling =====\n")

print("GRID:")
for row in grid:
    print(row)

print("\nStart State:", (start.x,start.y))
print("Goal State :", (goal.x,goal.y))

print("\nObstacle Positions:")
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            print((i,j))

print("\nEnvironment Successfully Modeled")