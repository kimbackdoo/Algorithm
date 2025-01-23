function solution(s) {
    let answer = 1
    for (let i = 0; i < s.length; i++) {
        answer = Math.max(
            answer,
            palindromeLength(s, i, i + 1),
            palindromeLength(s, i - 1, i + 1)
        )
    }
    
    return answer
}

function palindromeLength(s, left, right) {
    let [l, r] = [left, right]
    while (0 <= l && r < s.length && s[l] === s[r]) {
        l -= 1
        r += 1
    }
    
    return r - l - 1
}