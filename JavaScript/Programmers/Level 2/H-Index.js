// H-Index는 주어진 논문들의 인용횟수를 내림차순 한 후 인덱스 값이 해당 요소 값 이상이면 해당 인덱스 값이 h-index가 됨

function solution(citations) {
    citations.sort((a, b) => b - a); // 내림차순 정렬
    for (let i = 0; i < citations.length; i++) {
        if (i >= citations[i]) return i; // 인덱스 값이 해당 요소의 값 이상이면 인덱스 return
    }
    return citations.length; // 인덱스 값이 큰 경우가 없다면 citations의 길이 return
}
