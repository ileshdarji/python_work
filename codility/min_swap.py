def solution(S, T,):
    xy, yx = 0, 0
    for item1, item2 in zip(S, T):
        if item1 == 'x' and item2 == 'y':
            xy += 1
        elif item1 == 'y' and item2 == 'x':
            yx += 1
    if (xy + yx)%2 == 1:
        return -1
    return xy //2 + yx // 2 + xy % 2 + yx % 2

