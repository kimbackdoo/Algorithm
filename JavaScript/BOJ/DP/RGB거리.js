const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [N, ...arr] = fs.readFileSync(path).toString().trim().split('\n')
const n = Number(N)
const rgb = arr.map((value) => value.split(' ').map(Number))

function solution(n, rgb) {
    const dp = Array.from(Array(n), () => Array(3).fill(0))
    dp[0] = rgb[0]

    for (let i = 1; i < n; i++) {
        dp[i][0] = rgb[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = rgb[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = rgb[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1])
    }

    console.log(Math.min(...dp[n - 1]))
}

solution(n, rgb)