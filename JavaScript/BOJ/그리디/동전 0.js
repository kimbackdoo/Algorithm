const fs = require('fs')
const [NK, ...A] = fs.readFileSync('./test.txt').toString().trim().split("\n")
const [N, K] = NK.split(" ").map(Number)
const arr = A.map(Number)

function solution(N, K, arr) {
    const answer = arr.sort((a, b) => b - a).reduce((result, value) => {
        return [result[0] % value, result[1] + Math.floor(result[0] / value)]
    }, [K, 0])[1]

    console.log(answer)
}

solution(N, K, arr)