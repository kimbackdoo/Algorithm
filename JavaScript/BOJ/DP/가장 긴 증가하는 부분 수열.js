const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [N, arr] = fs.readFileSync(path).toString().trim().split('\n')
const n = Number(N)
const a = arr.split(' ').map(Number)

function solution(n, a) {
    const dp = Array(n).fill(1)

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (a[i] <= a[j]) continue
            dp[i] = Math.max(dp[i], dp[j] + 1)
        }
    }

    console.log(Math.max(...dp))
}

solution(n, a)