// 주어진 sides를 오름차순 정렬 후, 삼각형 조건 공식 적용
// class Solution {
//     fun solution(sides: IntArray): Int {
//         sides.sort()
//         val (x, y, z) = sides
//         return if (x + y > z) 1 else 2
//     }
// }

// let 메소드를 사용한 풀이
class Solution {
    fun solution(sides: IntArray): Int {
        return sides.sorted().let { (x, y, z) -> if (x + y > z) 1 else 2 }
    }
}
