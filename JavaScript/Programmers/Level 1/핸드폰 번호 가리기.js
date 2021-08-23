// 뒤에 4자리 빼고 "*"로 변환

// function solution(phone_number) {
//     // slice 메소드를 이용하여 뒤에 4자리를 빼고 잘라냄, replace 메소드를 이용하여 모든 숫자 *로 변환, 이때 g: 문자열 전체를 대상으로 검색, \d: 숫자
//     // 변환한 문자열과 뒤에 4자리를 합쳐서 return
//     return phone_number.slice(0, -4).replace(/\d/g, "*") + phone_number.slice(-4);
// }

// function solution(phone_number) {
//     // 정규식을 이용하여 한번에 해결
//     // \d: 숫자, x(?=y): y가 뒤따라오는 x 매칭, 즉, x 뒤에 반드시 y가 있어야함, \d{n}: 숫자가 n번 반복됨, g: 문자열 전체를 대상으로 검색
//     // 따라서, 문자열에서 뒤에서 숫자 4개를 제외하고 전부 *로 변환
//     return phone_number.replace(/\d(?=\d{4})/g, "*");
// }

function solution(phone_number) {
    // repeat 메소드를 이용하여 뒤에 *를 문자열의 길이 - 4 만큼 반복하고 뒤에 숫자 4자리를 합쳐서 return
    return "*".repeat(phone_number.length - 4) + phone_number.slice(-4);
}
