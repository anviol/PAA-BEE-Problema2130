import sys

INF = 10**15

def read_all_ints():
    data = sys.stdin.read().split()  # aceita linhas em branco sem problemas
    return list(map(int, data))

def build_snapshots(n, dist):
    snapshots = [[row[:] for row in dist]]  # k = 0

    for k in range(1, n + 1):
        prev = snapshots[-1]
        new_d = [row[:] for row in prev]
        for i in range(1, n + 1):
            dik = prev[i][k]
            if dik >= INF:
                continue
            pj = prev[k]
            nd_i = new_d[i]
            for j in range(1, n + 1):
                cand = dik + pj[j]
                if cand < nd_i[j]:
                    nd_i[j] = cand
        snapshots.append(new_d)
    return snapshots

def solve_instances(nums):
    out = []
    i = 0
    inst = 1
    L = len(nums)

    while i < L:
        if i + 1 >= L:
            break
        n = nums[i]; m = nums[i+1]; i += 2

        # matriz dist (1-indexed)
        dist = [[INF] * (n + 1) for _ in range(n + 1)]
        for v in range(1, n + 1):
            dist[v][v] = 0

        for _ in range(m):
            if i + 2 >= L:
                return out
            u = nums[i]; v = nums[i+1]; w = nums[i+2]; i += 3
            if w < dist[u][v]:
                dist[u][v] = w

        if i >= L:
            break
        c = nums[i]; i += 1

        queries = []
        for _ in range(c):
            if i + 2 >= L:
                break
            o = nums[i]; d = nums[i+1]; t = nums[i+2]; i += 3
            queries.append((o, d, t))

        snapshots = build_snapshots(n, dist)

        # Cabeçalho SEM linha em branco depois
        out.append(f"Instancia {inst}")

        for (o, d, t) in queries:
            if t < 0:
                t = 0
            elif t > n:
                t = n
            ans = snapshots[t][o][d]
            out.append(str(ans if ans < INF else -1))

        # Uma linha em branco APÓS a instância
        out.append("")
        inst += 1

    return out

def main():
    nums = read_all_ints()
    res = solve_instances(nums)
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()