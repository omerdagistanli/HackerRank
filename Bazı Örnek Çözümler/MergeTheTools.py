def merge_the_tools(string, k):
    kelime = ""
    l = len(string)
    loop = int(l / k)
    ek = 0
    yk = k
    for x in range(loop):
        for j in range(ek, yk):
            if l == 0:
                kelime += string[j]
            else:
                if string[j] not in kelime:
                    kelime += string[j]
        print(kelime)
        kelime = ""
        ek = yk
        yk += k

string, k = input(), int(input())
merge_the_tools(string, k)