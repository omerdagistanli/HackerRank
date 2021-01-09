def divisibleSumPairs(n, k, ar):
    ar.sort()
    sc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                sc += 1
    print(sc)

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    divisibleSumPairs(n, k, ar)