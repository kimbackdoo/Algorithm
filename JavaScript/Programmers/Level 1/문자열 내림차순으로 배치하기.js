// 주어진 문자열을 내림차순 정렬

// function compare(a, b) { // sort 메소드에 들어갈 compare 함수
//     if (a > b) {
//         return -1;
//     } else if (a === b) {
//         return 0;
//     } else {
//         return 1;
//     }
// }

// function solution(s) {
//     // s를 배열로 변환 후 내림차순 정렬 후 다시 문자열로 join
//     return s.split("").sort((a, b) => compare(a, b)).join("");
// }

// compare 함수를 만들지 않고 삼항연산자 이용

// function solution(s) {
//     return s.split("").sort((a, b) => a > b ? -1 : 1).join("");
// }

// sort 메소드는 아스키코드값을 기준으로 오름차순 정렬하므로 오름차순 정렬 후 reverse 메소드를 사용하면 내림차순 정렬됨

function solution(s) {
    // s를 배열로 변환 후 오름차순 정렬 후 reverse하여 내림차순 정렬, 이후 다시 문자열로 join
    return s.split("").sort().reverse().join("");
}
