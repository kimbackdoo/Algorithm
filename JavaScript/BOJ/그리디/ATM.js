const fs = require('fs')
const [N, P] = fs.readFileSync('/dev/stdin').toString().trim().split("\n")
const arr = P.split(" ").map(Number)

function solution(N, arr) {
    const sortedArr = arr.sort((a, b) => a - b)

    const answer = sortedArr.reduce((result, _, index) => {
        return result + arr.slice(0, index + 1).reduce((acc, cur) => acc + cur, 0)
    }, 0)

    console.log(answer)
}

solution(N, arr)