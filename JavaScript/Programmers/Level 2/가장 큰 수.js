// 배열의 최대 크기가 100,000이므로 모든 경우를 찾으면 시간초과됨을 예상할 수 있다.
// 자바스크립트에서 sort 메소드는 기본적으로 아스키 코드값을 기준으로 오름차순 정렬하므로 단순히 정렬을 하게 되면 원하는 결과가 안나옴
// 예를 들어, numbers가 [3, 30, 34, 5, 9]라면 정렬 결과는, [3, 30, 34, 5, 9]가 됨
// numbers의 요소의 최대값은 1000이므로 numbers의 모든 요소를 4자리로 늘린 후 정렬

// function solution(numbers) {
//     // numbers의 모든 요소를 [요소, 4자리 늘린 요소]로 mapping
//     // new Array를 이용하여 배열의 크기를 4로 지정하고, fill 메소드를 이용하여 모든 요소를 num으로 채움
//     // 이후 join 메소드를 이용하여 문자열로 변환 후 slice 메소드를 이용하여 4자리만 잘라냄
//     const answer = numbers.map(num => [num + "", new Array(4).fill(num + "").join("").slice(0, 4)])
//         .sort((a, b) => b[1] - a[1]) // 매핑한 결과 배열에서 4자리로 늘린 요소를 기준으로 내림차순 정렬
//         .map(item => item[0]) // map 메소드를 이용하여 원래 numbers의 요소만 남김
//         .join(""); // join 메소드를 이용하여 문자열로 변환
    
//     return !(+answer) ? "0" : answer; // numbers의 모든 요소가 0인 경우 answer은 "00.." 가 되므로 answer를 int로 바꾼 값이 0이라면 "0", 아니라면 answer return
// }

// 자바스크립트에서 sort 메소드는 아스키 코드값을 기준으로 오름차순 정렬하는 것을 이용하여
// numbers의 모든 요소를 4자리로 늘리는 것이 아닌 numbers의 요소를 이어붙였을 때를 기준으로 내림차순 정렬

function solution(numbers) {
    const answer = numbers.sort((a, b) => `${b}${a}` - `${a}${b}`).join(""); // a, b의 요소를 이어붙인 것을 기준으로 내림차순 정렬 후 문자열로 변환
    return answer[0] === "0" ? "0" : answer; // answer의 첫번째 요소가 "0"이라면 "0", 아니라면 answer return
}
