// function solution(babbling) {
//     const possibleBabblings = ["aya", "ye", "woo", "ma"]
    
//     return babbling
//         .map((b) => {
//             possibleBabblings.forEach((p) => { b = b.replace(p, " ") })
//             return b
//         })
//         .filter((b) => !b.trim())
//         .length
// }

function solution(babbling) {
    let answer = 0
    const possibleBabblings = ["aya", "ye", "woo", "ma"]
    
    babbling.forEach((b) => {
        possibleBabblings.forEach((pb) => {
            b = b.replace(pb, ".")
        })
        
        const dotCount = b.split(".").length - 1
        if (dotCount === b.length) answer++
    })
    
    return answer
}