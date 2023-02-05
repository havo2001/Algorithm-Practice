def length(a, b, c, d):
    return abs(a - c) + abs(b - d)


def BFS(vertice, coord, source, target, maxFuel):
    visited = [False] * vertice
    queue = []
    count = 0

    if source == target:
        return 0

    visited[source] = True
    queue.append([source, count])


    while len(queue) != 0:
        u = queue[0][0]
        count = queue[0][1]
        queue.pop(0)

        if u == target:
            return count

        for v in range(vertice):
            if visited[v] == False and length(coord[2 * u], coord[2 * u + 1], coord[2 * v], coord[2 * v + 1]) <= maxFuel:
                visited[v] = True
                queue.append([v, count + 1])

    return -1




n = int(input())
coord = []
for i in range(n):
    x, y = input().split(" ")
    coord.append(int(x))
    coord.append(int(y))
maxFuel = int(input())
x, y = input().split(" ")
source = int(x) - 1
target = int(y) - 1

print(BFS(n, coord, source, target, maxFuel))

