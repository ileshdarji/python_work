from packaging import version

def solution(S, T):
    if version.parse(S) > version.parse(T):
        return "1"
    if version.parse(S) < version.parse(T):
        return "-1"
    else:
        return "0"


print(solution("0.1", "1.1"))
print(solution("1.0.1", "1"))
print(solution("7.5.2.4", "7.5.3"))
print(solution("1.01", "1.001"))
print(solution("1.0", "1.0.0"))

# cmp = lambda x, y: version.parse(x).
# cmp("1.01", "1.001")
