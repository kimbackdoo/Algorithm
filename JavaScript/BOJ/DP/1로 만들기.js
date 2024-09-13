const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const N = Number(fs.readFileSync(path).toString().trim())

// function solution(N) {
//     const calculate = (N) => {
//         if (N in dp) return dp[N]

//         dp[N] = Math.min(
//             calculate(N - 1),
//             N % 2 === 0 ? calculate(N / 2) : Infinity,
//             N % 3 === 0 ? calculate(N / 3) : Infinity,
//         ) + 1
//         return dp[N]
//     }

//     const dp = { 1: 0, 2: 1, 3: 1 }

//     for (let i = 4; i <= N; i++) {
//         calculate(i)
//     }
    
//     console.log(dp[N])
// }

function solution(N) {
    const dp = { 1: 0, 2: 1, 3: 1 }

    for (let i = 4; i <= N; i++) {
        dp[i] = Math.min(
            dp[i - 1],
            i % 2 === 0 ? dp[i / 2] : Infinity,
            i % 3 === 0 ? dp[i / 3] : Infinity,
        ) + 1
    }
    
    console.log(dp[N])
}

solution(N)