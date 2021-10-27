def solution(grid):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    route = {}
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                x, y = i, j
                cnt, idx = 0, k
                tmp = []
                if not visited[x][y][idx]:
                    while True:
                        visited[x][y][idx] = True
                        if grid[x][y] == "L": idx = (idx - 1) % 4
                        elif grid[x][y] == "R": idx = (idx + 1) % 4
                        
                        x += move[idx][0]
                        y += move[idx][1]
                        tmp.append((x, y))
                        x, y = (x % len(grid)), (y % len(grid[0]))
                        cnt += 1

                        if x == i and y == j and idx == k:
                            break

                    if tuple(sorted(tmp)) not in route:
                        route[tuple(sorted(tmp))] = cnt
    
    return sorted([v for _, v in route.items()])
