def print_rangoli(n):
    cizgi_listem = []
    j = 0
    c = ""
    for i in range(1, n + 1):
        cizgi_listem += [{i : j}]
        j += 2
    print(cizgi_listem[n-1][n])
    for i in range(n,1,-1):
        print(chr(n+96).center(cizgi_listem[n-1][n] * 2 + 1, "-"))


# for i in range(int((kucuk - 1) / 2)):
#     print(((2*i+1)*c).center(buyuk,"-"))
#
# print(("WELCOME").center(buyuk,"-"))
#
# for i in range(int((kucuk - 1) / 2)-1, -1, -1):
#     print(((2*i+1)*c).center(buyuk,"-"))





n = int(input())
print_rangoli(n)