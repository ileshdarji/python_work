def solution(S: str, T: str) -> int:
    s = [int(x) for x in S.split('.')]
    t = [int(x) for x in T.split('.')]

    for x in range(max(len(s), len(t))):
        if x < len(s):
            S = s[x]
        else:
            S = 0

        if x < len(t):
            T = t[x]
        else:
            T = 0

        if s > t:
            return 1
        elif s < t:
            return -1

    return 0


print(solution("0.1", "1.1"))
print(solution("1.0.1", "1"))
print(solution("7.5.2.4", "7.5.3"))
print(solution("1.01", "1.001"))
print(solution("1.0", "1.0.0"))

# cmp = lambda x, y: version.parse(x).
# cmp("1.01", "1.001")
