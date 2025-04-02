currentChannel = 100

N = int(input())
M = int(input())

if M == 0:
    broken = []
else:
    broken = list(map(int, input().split()))


def isClickable(num):
    if num < 0:
        return False

    for n in broken:
        if str(n) in str(num):
            return False

    return True


def solve():
    if N == currentChannel:
        print(0)
        return

    if isClickable(N):
        res = min(abs(currentChannel - N), len(str(N)))
        print(res)
        return

    if M == 10:
        print(abs(currentChannel - N))
        return

    minCount = int(1e9)
    diff = 1
    while True:
        if isClickable(N - diff):
            minCount = len(str(N - diff)) + diff
            break
        elif isClickable(N + diff):
            minCount = len(str(N + diff)) + diff
            break
        else:
            diff += 1

    minCount = min(minCount, abs(currentChannel - N))

    print(minCount)


solve()
