# def birthday(arr, day, month, n):
#     total = 0
#     sc = 0
#     for x in range(n):
#         for i in range(x, month):
#             total += arr[i]
#             x = i
#         if total >= day:
#             sc += 1
#         total = 0
#         if month != arr[n-1]:
#             month += 1
#
#     print(sc)

def getWays(squares, d, m):
    tp = (len(squares)-m) + 1 #total number of pieces possible
    return len([1 for i in range(tp) if sum(squares[i:i+m])==d])



n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

day = int(dm[0])

month = int(dm[1])

result = getWays(arr, day, month)
print(result)

# birthday(arr, day, month, n)