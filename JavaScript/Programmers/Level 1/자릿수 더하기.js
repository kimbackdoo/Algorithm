// n의 모든 자리수를 더하면 됨
// n을 문자열로 변환 후 배열로 변환, 이후 reduce 메소드를 이용하여 합을 구함
// 문자열을 숫자로 변환 -> parseInt(), Number(), +, * 연산자 이용

// function solution(n) {
//     return [...(n + "")].reduce((sum, current) => sum + +current, 0);
// }


// function solution(n) {
//     return [...(n + "")].reduce((sum, current) => sum + current * 1, 0);
// }


function solution(n) {
    return [...(n + "")].reduce((sum, current) => sum + parseInt(current), 0);
}
