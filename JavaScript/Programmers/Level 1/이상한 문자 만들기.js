// 공백을 기준으로 나누어진 단어에서 인덱스가 짝수면 대문자로, 홀수면 소문자로 변환

function solution(s) {
    return s.split(" ") // split 메소드를 이용하여 공백을 기준으로 배열 변환
        // map 메소드를 이용하여 배열 요소 변환
        // 배열 요소는 단어이기 때문에 전개문법을 이용하여 단어를 배열로 변환 후 인덱스에 맞게 해당 알파벳 대소문자 변환 후 문자열로 join 
        .map(w => [...w].map((a, i) => !(i % 2) ? a.toUpperCase() : a.toLowerCase()).join(""))
        .join(" "); // 모든 요소를 변환 후 공백을 기준으로 join
}
