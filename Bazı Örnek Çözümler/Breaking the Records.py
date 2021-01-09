def breakingRecords(scores, n):
    max = 0
    min = 0
    score = scores[0]
    minscore = scores[0]
    for i in range(1, n):
        if score < scores[i]:
            max += 1
            score = scores[i]
        elif minscore > scores[i]:
            min += 1
            minscore = scores[i]
        else:
            pass

    print(max, min)

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    breakingRecords(scores, n)