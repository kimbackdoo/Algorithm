// n의 자리수를 뒤집은 배열 return

// function solution(n) {
//     // n을 문자열 변환 후 배열로 변환, 이후 reverse 메소드를 이용하여 배열을 뒤집고, map 메소드를 이용하여 모든 요소를 문자에서 숫자로 변환
//     return [...(n + "")].reverse().map(num => +num);
// }

// % 연산자를 이용하여 n을 10으로 나눈 나머지를 answer에 push
// answer에는 n의 끝자리부터 들어가므로 자동으로 뒤집은 배열이 됨

function solution(n) {
    const answer = [];
    while (n > 0) {
        answer.push(n % 10); // n의 나머지 push, n의 끝자리부터 들어감
        n = parseInt(n / 10); // 몫을 구하고 소수점을 버림, Math.floor를 사용해도 됨
    }
    
    return answer;
}
