// toString(base) 메소드를 사용하여 n을 3진법 문자열로 변환
// split() 메소드를 이용하여 문자열을 배열로 변환, reverse() 메소드를 이용하여 배열 뒤집기, join() 메소드를 이용하여 배열을 다시 문자열로 변환
// parseInt(num, base) 메소드를 이용하여 base진수 문자열을 숫자로 변환

// function solution(n) {
//     let answer = n.toString(3); // n을 3진수로 변환
//     answer = answer.split("").reverse().join(""); // answer을 배열로 변환 후 뒤집고 다시 문자열로 변환
//     return parseInt(answer, 3); // 3진수 문자열을 10진수로 변환
// }

function solution(n) {
    // 전개문법을 사용하여 3진수로 변환한 문자열을 배열로 변환 후 뒤집고 다시 문자열로 변환
    return parseInt([...n.toString(3)].reverse().join(""), 3);
}
