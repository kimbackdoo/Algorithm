// dfs
function solution(tickets) {
    const graph = tickets.reduce((result, [from, to]) => ({ ...result, [from]: [...(result[from] ?? []), to] }), {})
    Object.keys(graph).forEach((key) => graph[key].sort())

    const answer = []
    const dfs = (to) => {
        while (graph[to] && graph[to].length > 0) {
            const from = graph[to].shift()
            dfs(from)
        }
        answer.push(to)
    };

    dfs("ICN")
    return answer.reverse()
}