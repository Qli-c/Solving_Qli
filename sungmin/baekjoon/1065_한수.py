def isHanNumber(num):
    if num < 10:
        return True

    numli = list(str(num))

    # 공차
    diff = int(numli[1]) - int(numli[0])
    for i in range(1, len(numli)):
        newDiff = int(numli[i]) - int(numli[i - 1])
        if diff != newDiff:
            return False

    return True


n = int(input())

hansuNum = 0
for i in range(1, n + 1):
    if isHanNumber(i):
        hansuNum += 1

print(hansuNum)
