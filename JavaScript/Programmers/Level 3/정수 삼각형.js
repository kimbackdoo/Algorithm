// Bottom-Up DP
// 삼각형을 뒤집어서 큰 값들만 계산하면 됨
// 모든 값을 계산해서 배열에 저장하면 배열의 크기가 감당을 못함
function solution(triangle) {
    for(i = triangle.length - 2; i >= 0; i--) {
        for (j = 0; j < triangle[i].length; j++) {
            triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1])
        }
    }
    
    return triangle[0][0]
}