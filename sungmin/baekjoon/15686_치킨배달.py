from itertools import combinations

n, m = map(int, input().split())

chickens = []
houses = []

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == "1":
            houses.append((i, j))
        if line[j] == "2":
            chickens.append((i, j))


def calcDist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def solveWithCombination():
    combi = combinations(chickens, m)
    chickenDistance = 123456789
    for realChickens in combi:
        ds = 0
        for house in houses:
            minD = 123456789
            for chicken in realChickens:
                minD = min(minD, calcDist(house, chicken))
            ds += minD
        chickenDistance = min(chickenDistance, ds)

    print(chickenDistance)


def solveWithBacktracking():
    arr = []
    result = 123456789

    # num: 타겟 인덱스
    # cnt: 깊이
    def backtracking(num, cnt):
        nonlocal result

        if num > len(chickens):
            return

        if cnt == m:
            # 여기에 메인 로직 작성
            cityDistance = 0
            for house in houses:
                minD = 123456789
                for idx in arr:
                    chicken = chickens[idx]
                    minD = min(minD, calcDist(house, chicken))
                cityDistance += minD

            result = min(result, cityDistance)
            return

        arr.append(num)
        backtracking(num + 1, cnt + 1)

        # 방문했으면 제거하고 다음으로 넘어감
        arr.pop()
        backtracking(num + 1, cnt)

    backtracking(0, 0)

    print(result)


solve = solveWithBacktracking
solve()
