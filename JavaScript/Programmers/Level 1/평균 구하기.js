function solution(arr) {
    return arr.reduce((sum, current) => sum + current, 0) / arr.length; // reduce 메소드를 이용하여 arr의 합을 구하고, arr의 길이만큼 나누어 평균을 구함
}
