// n이 x의 제곱인지 아닌지 확인
// parseInt 함수를 사용하여 n의 제곱근이 정수인지 확인

// function solution(n) {
//     // n의 제곱근이 정수면 n의 제곱근 + 1의 제곱 return, 아니면 -1 return
//     return parseInt(n ** 0.5) === n ** 0.5 ? (n ** 0.5 + 1) ** 2 : -1;
// }

function solution(n) {
    // % 연산자를 활용하여 1로 나눈 나머지를 확인하면 n의 제곱근이 정수인지 확인할 수 있음
    return !((n ** 0.5) % 1) ? (n ** 0.5 + 1) ** 2 : -1;
}
