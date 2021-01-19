def countingValleys(steps, path):
    liste = []
    count = 0
    valley = 0
    liste += [int(-1) if path[i] == "D" else int(1) for i in range(steps)]

    for i in liste:
        if count == 0 and liste[i] == 1:
            count += 1
        elif count == 0 and liste[i] == -1:
            valley += 1
            count -= 1
        if liste[i] == 1:
            count += 1
            print("+")
        elif liste[i] == -1:
            count -= 1
            print("-")
    print(count)

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    countingValleys(steps, path)