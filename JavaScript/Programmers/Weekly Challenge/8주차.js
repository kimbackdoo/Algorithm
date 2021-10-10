// sizes의 모든 요소 중 가로, 세로의 값 중 큰 값은 지갑의 가로, 작은 값은 지갑의 세로로 만들면 됨

// function solution(sizes) {
//     // sizes의 모든 요소를 순회하면서 지갑의 가로, 세로의 값을 구함
//     return Math.max(...sizes.map(size => Math.max(...size))) * Math.max(...sizes.map(size => Math.min(...size)));
// }

// reduce 메소드를 이용하여 구할 수도 있음
function solution(sizes) {
    const [row, col] = sizes.reduce(([r, c], [a, b]) => [Math.max(r, Math.max(a, b)), Math.max(c, Math.min(a, b))], [0, 0]);
    return row * col;
}
