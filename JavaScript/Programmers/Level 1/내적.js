// a, b의 내적은 a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + ... + a[n-1] * b[n-1]
// 배열의 요소를 하나의 값으로 도출해주는 reduce 메소드 이용
// a.reduce((accumulator, item, index, array)=> accumulator + (item * b[index]), 0);, 초기값을 설정해줘야 어떤 상황에서도 오류 발생 안함

function solution(a, b) {
    return a.reduce((sum, current, idx)=> sum + (current * b[idx]), 0); // reduce 메소드 이용
}
