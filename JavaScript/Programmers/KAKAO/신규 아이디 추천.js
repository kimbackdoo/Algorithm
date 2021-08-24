// 문제 요구에 맞게 구현

// function solution(new_id) {
//     let answer = new_id.toLowerCase(); // 1단계
//     answer = answer.replace(/[^a-z0-9-_.]/g, ""); // 2단계
//     answer = answer.replace(/[.]{2,}/g, "."); // 3단계
//     answer = answer.replace(/^[.]|[.]$/g, ""); // 4단계
//     answer = !answer ? "a" : answer; // 5단계
//     answer = answer.slice(0, 15).replace(/[.]$/g, ""); // 6단계, 6-1단계
//     answer = answer.length <= 2 ? answer + answer.slice(-1).repeat(3-answer.length) : answer; // 7단계
//     return answer;
// }

function solution(new_id) {
    const answer = new_id
        .toLowerCase() // 1단계
        .replace(/[^\w-.]/g, "") // 2단계
        .replace(/\.+/g, ".") // 3단계
        .replace(/^\.|\.$/g, "") // 4단계
        .replace(/^$/, "a") // 5단계, /^&/: 문자열의 시작과 끝 사이에 아무 문자도 없음, 즉, 빈 문자열일 경우 "A"로 변환
        .slice(0, 15).replace(/\.$/, ""); // 6단계, 6-1단계, slice 메소드는 [end] 값이 문자열의 길이보다 작을 경우 원래 문자열 반환, 클 경우 slice
    // 7단계, padEnd 메소드는 전체 길이가 첫 번째 인수가 될때까지 2번째 인수를 이어붙임
    // 즉, answer의 길이가 3이 될 때까지 answer[answer.length - 1]을 이어붙임
    return answer.padEnd(3, answer[answer.length - 1]);
}
