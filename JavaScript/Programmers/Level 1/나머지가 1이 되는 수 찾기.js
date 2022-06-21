// 1부터 n - 1까지 순회하면서 나머지가 1이 되는 수를 찾으면 됨
function solution(n) {
    for (let x = 1; x < n; x++) { // 1부터 n - 1까지 순회하면서
        if (n % x === 1) return x; // 나머지가 1이 되는 수 return
    }
}
