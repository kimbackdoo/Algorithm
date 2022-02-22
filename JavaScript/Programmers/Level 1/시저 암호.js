// 문자를 n만큼 뒤로 밀면 됨, "z"인 경우 1번 뒤로 밀면 "a"가 됨
// 알파벳은 26개 있으므로 % 연산자를 활용하여 "a" ~ "z", "A" ~ "Z"가 순환할 수 있도록 구현

// function solution(s, n) {
//     return [...s].map(alpha => { // 전개문법을 이용하여 문자열을 배열로 변환
//         const ascii = alpha.charCodeAt(0); // 현재 알파벳의 아스키 코드 값을 구함
//         let tmp = 0;
//         if ("A" <= alpha && alpha <= "Z") {
//             tmp = 65; // alpha가 대문자면 65
//         } else if ("a" <= alpha && alpha <= "z") {
//             tmp = 97; // alpha가 소문자면 97
//         }
        
//         // tmp가 0이라는 뜻은 공백이라는 뜻
//         // 삼항연산자를 이용하여 공백이면 공백 return, 알파벳이면 n만큼 뒤로 민 값에 해당하는 알파벳 return
//         return tmp ? String.fromCharCode((ascii - tmp + n) % 26 + tmp) : alpha;
//     }).join(""); // 배열을 다시 문자열로 join
// }

// 아스키 코드 값으로 변환하여 계산하지 않고 미리 알파벳 문자열을 선언 후 계산

// function solution(s, n) {
//     const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // 대문자 문자열
//     const lower = "abcdefghijklmnopqrstuvwxyz"; // 소문자 문자열
    
//     return [...s].map(a => {
//         const alpha = upper.includes(a) ? upper : lower; // a가 대문자면 upper, 소문자면 lower 저장
//         // alpha에서 a의 인덱스가 -1이라는 뜻은 공백이라는 뜻
//         // 삼항 연산자를 이용하여 공백이면 공백 return, 공백이 아니면 n만큼 뒤로 민 알파벳 return
//         return alpha.indexOf(a) === -1 ? a : alpha[(alpha.indexOf(a) + n) % 26];
//     }).join(""); // 배열을 다시 문자열로 join
// }

// reduce를 사용한 풀이
function solution(s, n) {
    return [...s].reduce((answer, alpha) => {
        if (alpha === " ") {
            return answer + alpha;
        } else {
            if (alpha === alpha.toUpperCase()) {
                return answer + String.fromCharCode((alpha.charCodeAt() + n - 65) % 26 + 65);
            } else if (alpha === alpha.toLowerCase()) {
                return answer + String.fromCharCode((alpha.charCodeAt() + n - 97) % 26 + 97);
            }
        }
    }, "");
}
