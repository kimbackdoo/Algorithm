// 문자열에서 n번째 인덱스 요소를 기준으로 오름차순 정렬, 이때 n번째 인덱스 요소가 같다면 문자열 전체를 대상으로 오름차순 정렬

// function compare(a, b) { // sort 메소드에 들어갈 compare 함수, a > b이면 1, 같으면 0, 작으면 -1 반환
//     if (a > b) {
//         return 1;
//     } else if (a === b) {
//         return 0;
//     } else {
//         return -1;
//     }
// }

// function solution(strings, n) {
//     // n번째 요소를 기준으로 오름차순 정렬, 이때 n번째 요소가 같다면 문자열 전체를 대상으로 오름차순 정렬
//     return strings.sort((a, b) => a[n] === b[n] ? compare(a, b) : compare(a[n], b[n]));
// }

// localeCompare 메소드 이용
// a.localeCompare(b)은 a가 b보다 크다면 1, 같다면 0, 작다면 -1
// 위에서 compare 함수를 만든 것보다 속도측면에서는 많이 느림

function solution(strings, n) {
    return strings.sort((a, b) => a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]));
}
