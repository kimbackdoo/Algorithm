const fs = require('fs')
const N = Number(fs.readFileSync('/dev/stdin').toString().trim())

// function solution(N) {
//     for (let i = 0; i <= Math.floor(N / 3); i++) {
//         for (let j = 0; j <= Math.floor(N / 5); j++) {
//             if (3 * i + 5 * j === N) {
//                 console.log(i + j)
//                 return
//             }
//         }
//     }

//     console.log(-1)
// }

function solution(N) {
    let answer = 0

    while (N % 5 !== 0 && N >= 0) {
        N -= 3
        answer++
    }

    if (N < 0) return console.log(-1)

    console.log(answer + N / 5)
}

solution(N)