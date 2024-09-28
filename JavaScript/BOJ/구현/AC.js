const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [T, ...arr] = fs.readFileSync(path).toString().trim().split('\n')
const t = Number(T)

function solution(t, arr) {
    const run = (n, p, x) => {
        const command = {
            isReversed: false,
            startIndex: 0,
            endIndex: x.length,
            R: () => command.isReversed = !command.isReversed,
            D: () => command.isReversed ? command.endIndex-- : command.startIndex++,
        }

        p.forEach((value) => command[value]())

        if (command.startIndex > command.endIndex) return console.log("error")
        
        const result = x.slice(command.startIndex, command.endIndex)
        console.log(`[${(command.isReversed ? result.reverse() : result).join(",")}]`)
    }


    for (let i = 0; i < t * 3; i += 3) {
        const p = arr[i].split("")
        const n = Number(arr[i + 1])
        const x = arr[i + 2].replace(/[\[\]]/g, "").split(",").filter(Boolean).map(Number)

        run(n, p, x)
    }

}

solution(t, arr)