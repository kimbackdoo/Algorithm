// a부터 b까지 모든 수를 더하면 됨
// a, b의 대소관계가 정해져 있지 않으므로 Math.min, Math.max 사용

// function solution(a, b) {
//     let answer = 0;
//     for (let i = Math.min(a, b); i <= Math.max(a, b); i++) { // a ~ b까지 합을 구함
//         answer += i;
//     }
        
//     return answer;
// }

// 1 ~ n까지 합은 n * (n + 1) / 2
// a ~ b까지 합은 (a + b) * (a - b + 1) / 2

function solution(a, b) {        
    return (a + b) * (Math.abs(a - b) + 1) / 2; // 공식 적용
}
