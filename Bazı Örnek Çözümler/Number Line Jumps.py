import sys
def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            print("YES")
            sys.exit()
    print("NO")

x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
kangaroo(x1, v1, x2, v2)