def countApplesAndOranges(s, t, a, b, apples, oranges):
    eListe = [a + apples[i] for i in range(len(apples))]
    pListe = [b + oranges[i] for i in range(len(oranges))]
    escore = 0
    pscore = 0
    for i in range(len(eListe)):
        if eListe[i] >= s and eListe[i] <= t:
            escore += 1
    for i in range(len(pListe)):
        if pListe[i] >= s and pListe[i] <= t:
            pscore += 1
    print(escore, pscore)

st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)