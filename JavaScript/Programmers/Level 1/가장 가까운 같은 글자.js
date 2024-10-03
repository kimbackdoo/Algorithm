// function solution(s) {
//     const cache = {}
//     const answer = []
//     ;[...s].forEach((char, index) => {
//         answer.push(char in cache ? index - cache[char] : -1)
//         cache[char] = index
//     })
    
//     return answer
// }

function solution(s) {
    const cache = {}
    return [...s].map((char, index) => {
        const count = char in cache ? index - cache[char] : -1
        cache[char] = index
        return count
    })
}