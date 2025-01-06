// dfs
// function solution(begin, target, words) {
//     if (!words.includes(target)) return 0
    
//     const visited = {}
//     let answer = Infinity
    
//     const dfs = (begin, count) => {
//         if (begin === target) {
//             answer = Math.min(answer, count)
//             return
//         }
        
//         for (const word of words) {
//             if (!visited[word] && match(begin, word)) {
//                 visited[word] = true
//                 dfs(word, count + 1)
//                 visited[word] = false
//             }
//         }
//     }
    
//     dfs(begin, 0)
    
//     return answer === Infinity ? 0 : answer
// }

// bfs
function solution(begin, target, words) {
    if (!words.includes(target)) return 0
    
    const visited = { [begin]: 0 }
    const queue = [begin]
    while (queue.length > 0) {
        const currentWord = queue.shift()
        
        if (currentWord === target) return visited[target]
        
        for (const word of words) {
            if (!visited[word] && match(currentWord, word)) {
                queue.push(word)
                visited[word] = visited[currentWord] + 1
            }
        }
    }
    
    return 0
}

function match(a, b) {
    let result = 0
    for (let i = 0; i < a.length; i++) {
        if (a[i] === b[i]) continue
        result += 1
    }
    return result === 1
}