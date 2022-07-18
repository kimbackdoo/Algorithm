// arr에서 요소 2개씩 모든 요소의 최소공배수를 구하면 된다.

// function gcd(a, b) { // 최대공약수 구현, 유클리드 호제법 이용
//     [a, b] = [Math.max(a, b), Math.min(a, b)]; // a, b의 순서를 모르므로 a는 큰 수, b는 작은 수 저장
//     while (b) {
//         [a, b] = [b, a % b];
//     }
    
//     return a;
// }

// function solution(arr) {
//     while (arr.length > 1) { // arr의 요소가 한개가 남을때까지 반복
//         const [a, b] = [arr.shift(), arr.shift()]; // arr의 앞에서 2개 shift
//         arr.push((a * b) / gcd(a, b)); // a, b의 최소공배수를 구하고 push
//     }
    
//     return arr[0]; // n개의 최소공배수 return
// }

function gcd(a, b) { // 유클리드 호제법, 재귀로 구현
    return a % b ? gcd(b, a % b) : b;
}

function solution(arr) {
    // reduce 메소드를 이용하여 n개의 최소공배수를 구함
    // sum은 누적된 값이 저장되므로 항상 cur보다 크거나 같음
    // reduce 메소드의 2번째 인자로 초기값이 들어가는데 초기값이 없을 경우 arr의 첫번째 요소가 sum의 초기값이 됨
    // 예외가 발생하는 것을 방지하기 위해 arr을 slice 한 후, 초기값을 
    return arr.slice(1).reduce((sum, cur) => (sum * cur) / gcd(sum, cur), [arr[0]]);
}
