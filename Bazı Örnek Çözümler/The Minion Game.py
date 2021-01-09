def minion_game(string):
    stuart_score = stuart(string)
    kevin_score = kevin(string)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

def stuart(kelime):
    uzunluk = len(kelime)
    krktrListesi = []
    ch = ""
    score = 0

    for i in range(uzunluk):
        if kelime[i] != "A" and kelime[i] != "E" and kelime[i] != "I" and kelime[i] != "U":
            if krktrListesi.count(kelime[i]):
                # print("listede", kelime[i], "var")
                for i in range(len(krktrListesi)):
                    score += krktrListesi.count(kelime)
            else:
                # print("listede", kelime[i], "YOK")
                for j in range(uzunluk):
                    ch = kelime[i:j+1]
                    krktrListesi += [ch]

    return score

def kevin(kelime):
    uzunluk = len(kelime)
    krktrListesi = []
    ch = ""
    score = 0

    for i in range(uzunluk):
        if kelime[i] == "A" or kelime[i] == "E" or kelime[i] == "I" or kelime[i] == "U":
            if krktrListesi.count(kelime[i]):
                for x in range(len(krktrListesi)):
                    score += kelime.count(krktrListesi[x])
                for y in range(len(krktrListesi)):
                    if kelime[y:y + len(krktrListesi[y])] == krktrListesi[y]:
                        score += 1
                break
            else:
                for j in range(uzunluk):
                    ch = kelime[i:j + 1]
                    krktrListesi += [ch]

                while("" in krktrListesi):
                    krktrListesi.remove("")
    print(krktrListesi)
    print(score)
    return score

string = input()
minion_game(string)