// 문자열 내 p와 y의 개수를 비교, 대소문자 구문 안함

// function solution(s){
//     // match 메소드와 정규식을 이용하여 p와 y의 개수를 구함
//     // i 플래그: 대소문자 구분하지 않고 검색, g 플래그: 문자열 전체를 대상으로 검색
//     // p와 y의 개수가 없을 경우 즉, 정규식와 매칭되지 않을 경우 null이 반환되므로 null일 때는 빈 배열이 되게 함 
//     return (s.match(/p/ig) || []).length === (s.match(/y/ig) || []).length;
// }

// 문자를 대문자로 바꾼 후 P, S를 기준으로 split 후 길이 비교
// 예를 들어, "PPOOOYY"인 경우 P를 기준으로 split 하면 ["", "", "OOOYY"]가 됨
// 즉, split한 배열의 길이는 P의 개수 + 1이 됨을 이용

function solution(s){
    // s를 대문자로 변환 후 P, S를 기준으로 각각 split 후 길이 비교
    return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;;
}
