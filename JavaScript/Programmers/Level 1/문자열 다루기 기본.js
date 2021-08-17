// s의 길이가 4 또는 6이고, 숫자로만 이루어지면 true, 아니면 false return
// isNaN(s) 함수는 s가 문자면 true, 숫자면 false, 단 지수(1e9, 1e10, ...)나 16진수 같은 경우도 숫자로 인식
// 따라서 replace과 정규식을 이용하여 알파벳을 "_"으로 변환 후 숫자인지 문자인지 체크
// i 플래그: 대소문자 구분하지 않고 검색, g 플래그: 문자열 전체를 대상으로 검색

// function solution(s) {
//     return (s.length === 4 || s.length === 6) && !isNaN(s.replace(/[a-z]/ig, "_"));
// }

// 정규식 이용
// \d: 숫자, [0-9]와 똑같음, ^: 시작 부분, $: 끝 부분
// test 메소드는 정규식과 문자열이 매칭되면 true, 아니면 false return

function solution(s) {
    // s의 시작과 끝이 숫자 6개나 4개로 이루어진 경우 true, 아니면 false return
    return /^\d{6}$|^\d{4}$/.test(s);
}
