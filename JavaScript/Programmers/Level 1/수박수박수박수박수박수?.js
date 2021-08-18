// n = 3인 경우 "수박수", n = 4인 경우 "수박수박"
// 즉, "수박"을 (n + 1) / 2 만큼 반복하고 n까지 slice하면 됨

// function solution(n) {
//     const pattern = "수박";
//     let answer = "";
//     for (let i = 0; i < (n + 1) / 2; i++) { // (n + 1) / 2만큼 반복
//         answer += pattern;
//     }
    
//     return answer.slice(0, n); // n까지 slice
// }

// repeat 메소드를 이용하여 문자열 반복

function solution(n) {
    return "수박".repeat((n + 1) / 2).slice(0, n); // repeat 메소드를 이용하여 (n + 1) / 2만큼 반복하고 n까지 slice
}
