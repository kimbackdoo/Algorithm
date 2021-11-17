// s에서 최소값과 최대값을 찾으면 됨

// function solution(s) {
//     s = s.split(" ").map((item) => Number(item)); // s를 공백을 기준으로 split, 이후 s의 모든 요소를 숫자로 변환
//     return [Math.min(...s), Math.max(...s)].join(" "); // [s의 최소값, s의 최대값] 배열로 만든 후 join 메소드를 이용하여 공백을 기준으로 문자열로 변환
// }

function solution(s) {
    // Math.max, Math.min은 문자열 배열도 최대값, 최소값 찾아줌
    // 배열로 만들지 말고 바로 문자열 결합
    return Math.min(...s.split(" ")) + " " + Math.max(...s.split(" "));
}
