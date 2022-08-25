// 문제 요구에 따라 구현
// 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽, 모두 공백인 부분은 전체 지도에서도 공백
// 즉, 지도1, 2의 or 비트 연산을 통해 최종 지도를 구할 수 있다.

// function solution(n, arr1, arr2) {
//     return arr1.map((_, i) => { // map 메소드를 이용하여 최종지도를 한번에 구함
//         // arr1[i], arr2[i]의 or 비트연산 후 toString 메소드를 이용하여 2진수로 변환
//         // 이후 padStart 메소드를 이용하여 전체 길이가 n보다 작으면 앞에서 "0"을 채워 넣음
//         const result = (arr1[i] | arr2[i]).toString(2).padStart(n, "0");
//         // result 문자열을 전개문법을 이용하여 배열로 변환 후 각각의 요소가 "1"이면 "#", "0"이면 " "으로 매핑 후 다시 문자열로 변환
//         return [...result].map(bin => +bin ? "#" : " ").join("");
//     });
// }

function solution(n, arr1, arr2) {
    return arr1.map((_, i) =>
        // replace 메소드와 g(전역 플래그)를 이용하여 2진수로 변환된 문자열에서 0은 " "으로, 1은 "#"으로 변환
        (arr1[i] | arr2[i]).toString(2).padStart(n, "0").replace(/0/g, " ").replace(/1/g, "#")
   );
}
