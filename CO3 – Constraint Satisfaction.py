grid = [
['S','0','0','X','0'],
['0','X','0','X','0'],
['0','X','0','0','0'],
['0','0','X','X','0'],
['0','0','0','0','G']
]

path = [
(0,0),
(0,1),
(0,2),
(1,2),
(2,2),
(2,3),
(2,4),
(3,4),
(4,4)
]

print("===== CO3 : Constraint Validation =====\n")

print("GRID:")
for row in grid:
    print(row)

print("\nChecking Path...\n")

valid = True

for x,y in path:
    if grid[x][y] == 'X':
        print((x,y),"Constraint Failed")
        valid = False
        break
    else:
        print((x,y),"✓")

if valid:
    print("\nNo Constraint Violations")
    print("Valid Path Confirmed")