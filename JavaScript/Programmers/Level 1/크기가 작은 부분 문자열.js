// function getPartStrings(strings, targetLength) {
//     const result = []
//     for (let i = 0; i < [...strings].length; i++) {
//         if (strings.length - i < targetLength) return result
//         result.push(Number(strings.slice(i, i + targetLength)))
//     }
//     return result
// }

// function solution(t, p) {
//     const target = Number(p)
//     return getPartStrings(t, p.length).reduce((result, number) => result + Number(number <= target), 0)
// }

function solution(t, p) {
    let answer = 0
    for (let i = 0; i <= t.length - p.length; i++) {
        const part = Number(t.slice(i, i + p.length))
        if (part <= Number(p)) answer++
    }
    return answer
}