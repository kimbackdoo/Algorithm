// function solution(n, m, section) {
//     const walls = Array(n).fill(1)
    
//     section.forEach((item) => {
//         walls[item - 1] = 0
//     })
    
//     let answer = 0
//     for (let i = 0; i < n; i++) {
//         if (walls[i] === 1) continue
        
//         const length = i + m - 1
//         if (length >= n) {
//             answer++
//             break
//         }
        
//         for (let j = 0; j < m; j++) {
//             if (walls[i + j] === 1) continue
//             walls[i + j] = 1
//         }
//         answer++
//     }
    
//     return answer
// }

function solution(n, m, section) {
    let answer = 0
    let painted = 0
    for (const item of section) {
        if (painted >= item) continue
        painted = item + m - 1
        answer++
    }
    
    return answer
}