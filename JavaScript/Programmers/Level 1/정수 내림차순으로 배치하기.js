// 주어진 정수를 내림차순 정렬하면 됨
// 문자열을 숫자로 변환 -> parseInt(), Number(), +, * 연산자 이용

// function solution(n) {
//     // n을 문자열 변환 후 배열로 변환, 이후 내림차순 정렬 후, join메소드를 이용하여 문자열로 합침, 이후 + 연산자를 이용하여 문자열을 숫자로 변환
//     return +[...(n + "")].sort((a, b) => b - a).join("");
// }

function solution(n) {
    // Number을 사용하여 숫자로 변환
    return Number([...n.toString()].sort((a, b) => b - a).join(""));
}
