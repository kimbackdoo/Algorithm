const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [n, ...stairs] = fs.readFileSync(path).toString().trim().split('\n').map(Number)

function solution(n, stairs) {
    const getInitialDp = (n) => {
        const first = stairs[0]
        if (n === 1) return [first]

        const second = stairs[0] + stairs[1]
        if (n === 2) return [first, second]

        const third = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        return [first, second, third]
    }

    const dp = getInitialDp(n)

    for (let i = 3; i < n; i++) {
        dp.push(Math.max(
            dp[i - 2] + stairs[i],
            dp[i - 3] + stairs[i - 1] + stairs[i],
        ))
    }

    console.log(dp[n - 1])
}

solution(n, stairs)