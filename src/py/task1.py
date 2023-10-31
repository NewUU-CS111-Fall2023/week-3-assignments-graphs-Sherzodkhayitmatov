from collections import deque

def find_shortest_path(n, m, k, r, f):
    graph = [[] for _ in range(n + 1)]
    for x, y in r:
        graph[x].append(y)
        graph[y].append(x)
    f_set = set()
    for triplet in f:
        f_set.add((triplet[0], triplet[1], triplet[2]))
        f_set.add((triplet[1], triplet[0], triplet[2]))

    queue = deque([(1, [1])])

    visited = [False] * (n + 1)
    visited[1] = True

    while queue:
        city, path = queue.popleft()

        if city == n:
            return len(path) - 1, path

        for neighbor in graph[city]:
            if not visited[neighbor] and (city, city, neighbor) not in f_set:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))

    return -1, []

n, m, k = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(m)]
f = [tuple(map(int, input().split())) for _ in range(k)]

d, path = find_shortest_path(n, m, k, r, f)

if d == -1:
    print(-1)
else:
    print(d)
    print(*path)