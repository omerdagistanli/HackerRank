# import msvcrt

def catAndMouse(x, y, z):
    a = abs(x - z)
    b = abs(y - z)

    return "Cat A" if a < b else "Cat B" if b < a else "Mouse C"

q = int(input())

for q_itr in range(q):
    xyz = input().split()
    # xyz = msvcrt.getch()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = catAndMouse(x, y, z)
    print(result)