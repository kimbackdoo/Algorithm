function solution(arr1, arr2) {
    // map 메소드를 이용하여 덧셈하여 mapping, 2차원 배열이므로 map 메소드를 2번 사용해야 각 요소에 접근할 수 있음
    // map 메소드를 이용하여 행을 가져오고, 각 행을 다시 map 메소드를 이용하여 각 요소를 가져옴, 이후 arr1, arr2의 각 요소를 더한 결과를 return
    return arr1.map((_, i) => arr1[i].map((_, j) => arr1[i][j] + arr2[i][j]));
}
