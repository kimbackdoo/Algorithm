// Date 객체 사용하여 요일을 구함

// function solution(a, b) {
//     const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]; // Date 객체의 getDay 메소드는 0은 일요일 ~ 6은 토요일이므로 반환값에 맞게 요일 배열 생성
//     const answer = new Date(2016, a - 1, b); // Date 객체를 이용하여 2016년 a월 b일 날짜 생성, Date 객체에서 월은 0부터 시작하므로 a - 1로 설정
//     return day[answer.getDay()]; // answer.getDay()에 해당하는 값을 day 배열에서 가져옴
// }

// function solution(a, b) {
//     const days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]; // 1월 ~ 12월까지의 일수를 미리 구함
//     const week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
    
//     return week[(days.slice(0, a - 1).reduce((total, day) => total + day, 0) + b - 1) % 7] // ((a - 1)까지의 일수의 총합 + b - 1) % 7을 하여 현재 날짜의 인덱스를 구함
// }

// return문이 너무 길어져서 가독성이 떨어지므로
// sum 함수를 만들어 사용
function sum(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0);
}

function solution(a, b) {
    const days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
    
    return week[(sum(days.slice(0, a - 1)) + b - 1) % 7]
}
