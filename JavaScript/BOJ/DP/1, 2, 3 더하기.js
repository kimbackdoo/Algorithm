const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [T, ...numbers] = fs.readFileSync(path).toString().trim().split('\n').map(Number)

function solution(T, numbers) {
    for (let t = 0; t < T; t++) {
        const dp = { 1: 1, 2: 2, 3: 4 }
        for (let i = 4; i <= numbers[t]; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        }

        console.log(dp[numbers[t]])
    }
}

solution(T, numbers)