const fs = require('fs')
const path = process.platform === "linux" ? "/dev/stdin" : "./test.txt"
const [T, ...numbers] = fs.readFileSync(path).toString().trim().split('\n').map(Number)

function solution(T, numbers) {
    for (let t = 0; t < T; t++) {
        const dp = { 0: [1, 0], 1: [0, 1] }
        for (let i = 2; i <= numbers[t]; i++) {
            dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]
        }

        console.log(dp[numbers[t]].join(' '))
    }
}

solution(T, numbers)