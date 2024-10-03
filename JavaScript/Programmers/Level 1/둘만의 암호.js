// function solution(s, skip, index) {
//     const tmp = { a: true, b: true, c: true, d: true, e: true, f: true, g: true, h: true, i: true, j: true, k: true, l: true, m: true, n: true, o: true, p: true, q: true, r: true, s: true, t: true, u: true, v: true, w: true, x: true, y: true, z: true }
    
//     ;[...skip].forEach((char) => delete tmp[char])
//     const alphabet = Object.keys(tmp).join('')
//     const alphabetMap = Object.fromEntries(Object.entries(tmp).map(([char], index) => [char, index]))
    
//     return [...s].reduce((result, char) => `${result}${alphabet[(alphabetMap[char] + index) % alphabet.length]}`, "")
// }

function solution(s, skip, index) {
    const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"].filter((char) => !skip.includes(char))
    const alphabetMap = alphabet.reduce((result, char, index) => ({...result, [char]: index}) , {})
    
    return [...s].reduce((result, char) => `${result}${alphabet[(alphabetMap[char] + index) % alphabet.length]}`, "")
}