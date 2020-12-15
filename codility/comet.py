def solution(A):
    resp = []
    for item in A:
        while resp and item < 0 < resp[-1]:
            if resp[-1] < -item:
                resp.pop()
                continue
            elif resp[-1] == -item:
                resp.pop()
            break
        else:
            resp.append(item)
    return resp
