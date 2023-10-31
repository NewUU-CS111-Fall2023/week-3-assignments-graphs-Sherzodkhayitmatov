def dfs(frag, visited, c_g, min_g):
    if all(visited):
        if len(c_g) < len(min_g):
            return c_g
        return min_g

    for i in range(len(frag)):
        if not visited[i]:
            visited[i] = True
            if frag[i] in c_g:
                min_g = dfs(frag, visited, c_g, min_g)

            else:
                min_g = dfs(frag, visited, c_g + frag[i], min_g)
            visited[i] = False

    return min_g

n = int(input())
frag = []
for _ in range(n):
    frag = input().strip()
    frag.append(frag)
visited = [False] * n

current_genome = ""
min_g = "z" * (26 * n)
min_g = dfs(frag, visited, current_genome, min_g)
print(min_g)