const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [n, ...arr] = fs.readFileSync(path).toString().trim().split("\n")
const N = Number(n)
const times = arr.map((value) => value.split(" ").map(Number))

function solution(N, times) {
    times.sort((a, b) => {
        if (a[1] === b[1]) return a[0] - b[0]
        return a[1] - b[1]
    })

    const result = [times[0]]
    for (let i = 1; i < N; i++) {
        if (times[i][0] < result[result.length - 1][1]) continue
        result.push(times[i])
    }

    console.log(result.length)
}

solution(N, times)