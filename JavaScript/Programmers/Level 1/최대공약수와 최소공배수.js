// n, m의 최대공약수, 최소공배수를 구하면 됨

// function gcd(n, m) { // n, m의 최대공약수, 유클리드 호제법 이용
//     let [a, b] = [Math.min(n, m), Math.max(n, m)]; // n, m의 크기가 정해져 있지 않으므로 둘 중 작은 값을 a, 큰 값을 b에 저장, 구조분해할당 문법 사용
//     while (a) {
//         [a, b] = [b % a, a]; // 구조분해할당 문법을 사용하여 유클리드 호제법 구현
//     }
    
//     return b; // 최대공약수 return
// }

// function solution(n, m) {
//     const g = gcd(n, m);
//     return [g, (n * m) / g]; // 최대공약수와 최소공배수 return
// }

// 함수를 호출하는 쪽에서 최소값, 최대값을 정해서 호출함
function gcd(a, b) {
    while (!!a) [a, b] = [b % a, a]; // 유클리드 호제법 이용
    return b;
}

function solution(n, m) {
    const g = gcd(Math.min(n, m), Math.max(n, m));
    return [g, n * m / g];
}
