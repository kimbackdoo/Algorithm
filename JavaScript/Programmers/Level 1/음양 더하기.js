// reduce 메소드를 이용하여 값을 도출
// absolutes, signs의 길이는 같음

function solution(absolutes, signs) {
    return absolutes.reduce((sum, current, idx)=> sum + (signs[idx] ? current : -current), 0); // reduce 메소드를 이용하여 합을 구함, signs[idx] 값이 true면 양수, false면 음수
}
