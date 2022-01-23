// 문제 조건에 맞게 구현

// function solution(num) {
//     let answer = 0;
//     while (num !== 1 && answer < 500) { // num이 1이 될때까지 반복, answer 값은 500보다 작아야함
//         num = !(num % 2) ? num / 2 : num * 3 + 1; // 삼항연산자를 이용하여 짝수는 /2, 홀수면 *3 + 1 진행
//         answer++;
//     }
    
//     return answer < 500 ? answer : -1;
// }

// answer가 500이 되면 바로 return -1을 하여 마지막 return문에서 다시 조건을 따지지 않게함
function solution(n) {
    let answer = 0;
    while (n > 1) {
        if (answer === 500) return -1;
        n = !(n % 2) ? n / 2 : (n * 3) + 1;
        answer++;
    }
    return answer;
}
