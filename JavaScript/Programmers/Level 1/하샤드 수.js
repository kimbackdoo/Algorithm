function solution(x) {
    // x를 문자열로 변환 후 배열로 변환, 이후 reduce 메소드를 이용하여 x의 각 자리의 합을 구함
    const num = [...(x + "")].reduce((sum, c) => sum + +c, 0);
    return !(x % num); // 나누어 떨어진다면 하샤드 수
}
