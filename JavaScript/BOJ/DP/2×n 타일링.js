const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const n = Number(fs.readFileSync(path).toString().trim())

function solution(n) {
    const dp = { 1: 1, 2: 2 }
    for (let i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    }

    console.log(dp[n])
}

solution(n)