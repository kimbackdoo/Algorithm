// Date 객체 사용하여 요일을 구함

function solution(a, b) {
    const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]; // Date 객체의 getDay 메소드는 0은 일요일 ~ 6은 토요일이므로 반환값에 맞게 요일 배열 생성
    const answer = new Date(2016, a - 1, b); // Date 객체를 이용하여 2016년 a월 b일 날짜 생성, Date 객체에서 월은 0부터 시작하므로 a - 1로 설정
    return day[answer.getDay()]; // answer.getDay()에 해당하는 값을 day 배열에서 가져옴
}
