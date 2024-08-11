// 객체 또는 Map으로 그래프를 구현하면 런타임 에러(TypeError)가 발생함... 왜 그런지는 모르겠음
const fs = require('fs')
const input = fs.readFileSync(`${__dirname}/dev/stdin`).toString().trim().split("\n")
const [n, m, v] = input.shift().split(" ").map(Number)
const numbers = input.map((numbers) => numbers.split(" ").map(Number))

function generateGraph(numbers) {
    const graph = Array.from({ length: n + 1 }, () => [])

    numbers.forEach(([a, b]) => {
        graph[a].push(b)
        graph[b].push(a)
    })

    graph.forEach((edges) => {
        edges.sort((a, b) => a - b)
    })

    return graph
}

function bootstrap(cmd) {
    const graph = generateGraph(numbers)
    const result = []
    const visited = Array(n + 1).fill(false)

    const dfs = (v) => {
        visited[v] = true
        result.push(v)
        for (let i of graph[v]) {
            if (visited[i]) continue
            dfs(i)
        }
    }

    const bfs = (v) => {
        const queue = [v]
        visited[v] = true

        while (queue.length > 0) {
            const current = queue.shift()
            result.push(current)

            for (let i of graph[current]) {
                if (visited[i]) continue
                visited[i] = true
                queue.push(i)
            }
        }
    }

    switch (cmd) {
        case "dfs":
            dfs(v)
            break
        case "bfs":
            bfs(v)
            break
        default:
            break
    }

    console.log(result.join(" "))
}

bootstrap("dfs")
bootstrap("bfs")