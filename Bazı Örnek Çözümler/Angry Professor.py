def angryProfessor(istenen, arr, total):
    gecKalan = 0
    for i in range(total):
        if arr[i] > 0:
            gecKalan += 1

    if gecKalan >= istenen:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        total = int(nk[0])

        istenen = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        angryProfessor(istenen, arr, total)