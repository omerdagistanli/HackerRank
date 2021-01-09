def getMoneySpent(keyboards, usbs, b, klCount, usbCount):
    liste = []
    if klCount < usbCount:
        for i in range(klCount):
            for j in range(usbCount):
                liste += [keyboards[i] + usbs[j]]
    else:
        for i in range(usbCount):
            for j in range(klCount):
                liste += [usbs[i] + keyboards[j]]
    yeniListe = []
    for i in range(len(liste)):
        if liste[i] <= b:
            yeniListe += [liste[i]]
    if len(yeniListe) != 0:
        print(max(yeniListe))
    else:
        print("-1")

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    getMoneySpent(keyboards, drives, b, n, m)