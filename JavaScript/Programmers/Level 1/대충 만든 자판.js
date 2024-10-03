// function solution(keymap, targets) {    
//     const keys = {}
//     keymap.forEach((strings) => {
//         [...strings].forEach((key, index) => {
//             keys[key] = Math.min(keys[key] || Infinity, index + 1)
//         })
//     })
    
//     const answer = []
//     targets.forEach((strings) => {
//         let cnt = 0
//         ;[...strings].forEach((target) => cnt += keys[target])
//         answer.push(cnt || -1)
//     })
    
//     return answer
// }

function solution(keymap, targets) {    
    const keys = {}
    keymap.forEach((strings) => {
        [...strings].forEach((key, index) => {
            keys[key] = Math.min(keys[key] || Infinity, index + 1)
        })
    })
    
    const answer = []
    targets.forEach((strings) => {
        const count = [...strings].reduce((result, target) => result + keys[target], 0)
        answer.push(count || -1)
    })
    
    return answer
}