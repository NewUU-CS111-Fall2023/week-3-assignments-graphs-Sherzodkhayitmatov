from collections import defaultdict

def dfs(v, parent, d, g):
    for u in g[v]:
        if u != parent:
            d[u] = d[v] + 1
            dfs(u, v, d, g)
n, x = map(int, input().split())

graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distances = [0] * (n+1)

dfs(1, 0, distances, graph)

alice_moves = distances[x]
bob_moves = max(distances[i] for i in range(1, n+1) if i != x)
total_moves = 2 * bob_moves

print(total_moves)