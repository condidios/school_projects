import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
delta = (b**2 - 4*c*a)
if delta < 0:
    print("Neither of the soulutions are real numbers")
elif delta == 0:
    root1 = (-b) / (2*a)
    print("Has a repeated real number solution")
    print("Solution(s):" , root1 , root1)
else:
    rootDelta = delta**0.5
    int(rootDelta)
    root1 = (-b + rootDelta) / (2*a)
    root2 = (-b - rootDelta) / (2*a)
    print("There are two solutions")
    print("Solution(s):", root1, root2)



