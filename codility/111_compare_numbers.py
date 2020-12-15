def solution(S: str, T: str) -> int:
    s_list = [int(x) for x in S.split('.')]
    t_list = [int(x) for x in T.split('.')]

    len1 = len(s_list)
    len2 = len(t_list)

    for i in range(max(len1, len2)):
        i1 = int(s_list[i]) if i < len1 else 0

        i2 = int(t_list[i]) if i < len2 else 0

        if i1 != i2:
            return 1 if i1 > i2 else -1
    return 0


print(solution("0.1", "1.1"))
print(solution("1.0.1", "1"))
print(solution("7.5.2.4", "7.5.3"))
print(solution("1.01", "1.001"))
print(solution("1.0", "1.0.0"))

# cmp = lambda x, y: version.parse(x).
# cmp("1.01", "1.001")
