// 4개의 점들을 2개씩 그룹짓고,
// 공식을 이용하여 두 선분이 평행한지 확인

// typealias IntList = List<Int>
    
// class Solution {
//     fun solution(dots: Array<IntArray>): Int {
//         val listDots = dots.map { it.toList() }.toList()
//         val visited = MutableList(dots.size) { false }

//         val answer = dfs(listDots, listOf(), visited)
//         return if (answer) 1 else 0
//     }
  
//     // dfs
//     // origin의 요소를 모두 뽑음
//     private fun dfs(origin: List<IntList>, result: List<IntList>, visited: MutableList<Boolean>): Boolean {
//         if (result.size == origin.size) return isParallel(result)

//         for (i in origin.indices) {
//             if (visited[i]) continue
//             visited[i] = true
//             val found = dfs(origin, result + listOf(origin[i]), visited)
//             if (found) return true
//             visited[i] = false
//         }
//         return false
//     }

//     // 평행한지 확인하는 함수
//     private fun isParallel(dots: List<IntList>): Boolean {
//         val m1 = calculateSlope(dots[0], dots[1])
//         val m2 = calculateSlope(dots[2], dots[3])
//         return m1 == m2
//     }

//     // 기울기는 계산하는 함수
//     private fun calculateSlope(dot1: List<Int>, dot2: List<Int>): Double {
//         val x = dot2[0] - dot1[0]
//         val y = dot2[1] - dot1[1]
//         return y * 1.0 / x
//     }
// }

// dfs로 모든 요소를 확인하는 것이 아닌
// 4개의 점들 중, [1,2,3,4], [1,3,2,4], [1,4,2,3]을 확인하면 평행한지 아닌지 구할 수 있음
class Solution {
    fun solution(dots: Array<IntArray>): Int {
        if (isParallel(listOf(dots[0], dots[1], dots[2], dots[3]))) return 1
        if (isParallel(listOf(dots[0], dots[2], dots[1], dots[3]))) return 1
        if (isParallel(listOf(dots[0], dots[3], dots[1], dots[2]))) return 1
        return 0
    }

    private fun isParallel(dots: List<IntArray>): Boolean {
        val m1 = calculateSlope(dots[0], dots[1])
        val m2 = calculateSlope(dots[2], dots[3])
        return m1 == m2
    }

    private fun calculateSlope(dot1: IntArray, dot2: IntArray): Double {
        val (x1, y1) = dot1
        val (x2, y2) = dot2
        return (y2 - y1) * 1.0 / (x2 - x1)
    }
}
