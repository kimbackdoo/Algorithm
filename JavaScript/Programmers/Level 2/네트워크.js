// dfs
// function solution(n, computers) {
//     const visited = Array.from({ length: n }, () => false)
    
//     const dfs = (i) => {
//         visited[i] = true
//         for (let j = 0; j < computers[i].length; j++) {
//             if (!visited[j] && computers[i][j] === 1) {
//                 dfs(j)
//             }
//         }
//     }
    
//     let answer = 0
//     for (let i = 0; i < n; i++) {
//         if (!visited[i]) {
//             answer += 1
//             dfs(i)
//         }
//     }
    
//     return answer
// }

// bfs
function solution(n, computers) {
    const visited = Array.from({ length: n }, () => false)
    
    const bfs = (i) => {
        visited[i] = true
        const queue = [i]
        while (queue.length > 0) {
            const v = queue.shift()
            for (let j = 0; j < computers[v].length; j++) {
                if (!visited[j] && computers[v][j] === 1) {
                    visited[j] = true
                    queue.push(j)
                }
            }
        }
    }
    
    let answer = 0
    for (let i = 0; i < computers.length; i++) {
        if (!visited[i]) {
            answer += 1
            bfs(i)
        }
    }
    
    return answer
}