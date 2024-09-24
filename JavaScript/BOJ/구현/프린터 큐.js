const fs = require('fs')
const path = process.platform === 'linux' ? '/dev/stdin' : './test.txt'
const [T, ...arr] = fs.readFileSync(path).toString().trim().split('\n')
const t = Number(T)

function solution(t, arr) {
    const runPrint = (prints, m) => {
        let answer = 0
        while(prints.length > 0) {
            const current = prints.shift()
            const isPrint = prints.every(([_, value]) => value <= current[1])

            if (!isPrint) {
                prints.push(current)
                continue
            }

            if (current[0] === Number(m)) {
                return answer + 1
            }

            answer++
        }
    }

    for(let i=0; i < t * 2; i+=2) {
        const [n, m] = arr[i].split(' ')
        const prints = arr[i + 1].split(' ').map(Number).map((value, index) => [index, value])
        console.log(runPrint(prints, m))
    }

}

solution(t, arr)