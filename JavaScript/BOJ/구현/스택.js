const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [N, ...arr] = fs.readFileSync(path).toString().trim().split('\n')
const n = Number(N)

// function solution(n, arr) {
//     const stack = {
//         result: [],
//         arr: [],
//         isEmpty: () => stack.arr.length === 0,
//         push: (x) => stack.arr.push(x),
//         pop: () => stack.result.push(stack.isEmpty() ? -1 : stack.arr.pop()),
//         size: () => stack.result.push(stack.arr.length),
//         empty: () => stack.result.push(stack.isEmpty() ? 1 : 0),
//         top: () => stack.result.push(stack.isEmpty() ? -1 : stack.arr[stack.arr.length - 1]),
//     }

//     arr.forEach((item) => {
//         const [cmd, value] = item.split(' ')
//         stack[cmd](Number(value))
//     })

//     console.log(stack.result.join('\n'))
// }

function solution(n, arr) {
    const stack = {
        result: [],
        arr: [],
        push: (x) => stack.arr.push(x),
        pop: () => stack.result.push(stack.arr.pop() || -1),
        size: () => stack.result.push(stack.arr.length),
        empty: () => stack.result.push(stack.arr[0] ? 0 : 1),
        top: () => stack.result.push(stack.arr[stack.arr.length - 1] || -1),
    }

    arr.forEach((item) => {
        const [cmd, value] = item.split(' ')
        stack[cmd](Number(value))
    })

    console.log(stack.result.join('\n'))
}

solution(n, arr)