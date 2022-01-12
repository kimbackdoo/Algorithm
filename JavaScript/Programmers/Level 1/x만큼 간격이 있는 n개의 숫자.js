// x부터 시작하여 x씩 증가하는 숫자를 n개 가진 배열을 만들면 됨

// function solution(x, n) {
//     const answer = [];
//     for (let i = 1; i <= n; i++) {
//         answer.push(i * x); // i * x를 하게 되면 x씩 증가하는 숫자가 됨 즉, (현재 인덱스 + 1) * x
//     }
    
//     return answer;
// }

// function solution(x, n) {
//     // new Array를 이용하여 크기가 n인 배열을 만든 후, 모든 요소를 0으로 채움
//     // 이후, map 메소드를 이용하여 각 요소를 (각 요소의 인덱스 + 1) * x로 mapping
//     return new Array(n).fill(0).map((_, i) => (i + 1) * x);
// }

function solution(x, n) {
    // 길이가 n인 배열을 만들고 x로 채움
    // map 메소드를 이용하여 x씩 증가하게 만듦
    return Array(n).fill(x).map((num, index) => num * (index + 1));;
}
