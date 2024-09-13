const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const expr = fs.readFileSync(path).toString().trim()

function solution(expr) {
    const answer = expr
        .split("-")
        .map((value) => value.split("+").map(Number).reduce((acc, cur) => acc + cur, 0))
        .reduce((acc, cur) => acc - cur)

    console.log(answer)
}

solution(expr)