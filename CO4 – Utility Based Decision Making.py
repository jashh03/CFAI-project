grid = [
['S','0','0','X','0'],
['0','X','0','X','0'],
['0','X','0','0','0'],
['0','0','X','X','0'],
['0','0','0','0','G']
]

pathA = [
(0,0),(0,1),(0,2),
(1,2),(2,2),(2,3),
(2,4),(3,4),(4,4)
]

pathB = [
(0,0),(1,0),(2,0),
(3,0),(4,0),(4,1),
(4,2),(4,3),(4,4)
]

riskA = 8
riskB = 2

utilityA = 100 - len(pathA) - riskA
utilityB = 100 - len(pathB) - riskB

print("===== CO4 : Utility Decision =====\n")

print("GRID:")
for row in grid:
    print(row)

print("\nPath A:")
print(pathA)
print("Distance =",len(pathA))
print("Risk =",riskA)
print("Utility =",utilityA)

print("\n----------------------------")

print("\nPath B:")
print(pathB)
print("Distance =",len(pathB))
print("Risk =",riskB)
print("Utility =",utilityB)

print("\n----------------------------")

if utilityA > utilityB:
    print("\nBest Decision = Path A")
else:
    print("\nBest Decision = Path B")