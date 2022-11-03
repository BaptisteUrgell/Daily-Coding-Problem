def new_pos(m: list, M: int, N: int, pos: int):
    current = []
    if not m[pos]:
        m[pos] = True
        current.append(pos)
    return m, current


def daily(m: list, M: int, N: int, s: int, e: int):
    current = [[s]]
    m[s] = True

    for i in range(1, M*N):
        if e in current[-1]:
            return i
        for pos in current[-1]:
            up, down, left, right = [], [], [], []
            if not pos < M:
                m, up = new_pos(m, M, N, pos-M)
            if not pos >= (M-1) * N:
                m, down = new_pos(m, M, N, pos+M)
            if not pos % N == 0:
                m, left = new_pos(m, M, N, pos-1)
            if not pos % N == N - 1:
                m, right = new_pos(m, M, N, pos+1)
            nex_current = up + down + left + right
        if not nex_current:
            return None
        current.append(nex_current)
    return None



if __name__ == "__main__":

    default_args = {
        "m" : [False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, False],
        "s" : 13,
        "e" : 0,
        "M" : 4,
        "N" : 4
    }
    print(daily(default_args["m"], default_args["M"], default_args["N"], default_args["s"], default_args["e"]))

