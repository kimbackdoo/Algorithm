// 숫자에 해당하는 문자열을 숫자로 변환하면 됨

// function solution(s) {
//     // 문자열에 해당하는 숫자를 객체로 선언
//     const number = {zero: "0", one: "1", two: "2", three: "3",
//                  four: "4", five: "5", six: "6",
//                  seven: "7", eight: "8", nine: "9"};
    
//     for (let key in number) { // number의 모든 key를 순회
//         const regexAll = new RegExp(key, "g"); // new RegExp를 이용하여 key에 해당하는 패턴을 생성, 이때 g: 문자열 전체를 대상으로 검색하겠다는 뜻
//         s = s.replace(regexAll, number[key]); // replace 메소드와 등록된 패턴을 이용하여 문자열을 해당하는 숫자로 변환
//     }
    
//     return +s; // +연산자를 이용하여 문자열 s를 숫자로 변환
// }

function solution(s) {
    const number = {zero: "0", one: "1", two: "2", three: "3",
                 four: "4", five: "5", six: "6",
                 seven: "7", eight: "8", nine: "9"};
    
    for (let [key, value] of Object.entries(number)) { // Object.entries를 이용하여 number 객체를 [key, value] 배열로 변환, 배열이기 때문에 for of 사용
        const tmp = s.split(key); // key를 기준으로 split, 예를 들어, s가 "one2three4five"고, key가 "one"라면 ["", "2three4five"]가 됨
        s = tmp.join(value) // split 한 배열을 value를 기준으로 join, 위 예를 보면 "12three4five"가 됨
    }
    
    return +s;
}
