import sys
def flatlandSpaceStations(n, c):
    if len(c) == n:
        print("0")
        sys.exit()

    liste = []
    liste2 = []
    minListe = []
    liste += [i for i in range(n)]

    for i in c:
        liste.remove(i)

    for a in liste:
        for b in c:
            liste2 += [abs(a - b)]
        minListe += [min(liste2)]
        liste2 = []

    print(max(minListe))

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    flatlandSpaceStations(n, c)