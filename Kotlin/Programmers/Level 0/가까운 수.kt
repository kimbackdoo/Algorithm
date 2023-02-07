// 주어진 array를 순회하면서 n과의 차를 구하고 오름차순 정렬
// 이때 차가 같을 수 있으므로 abs 함수를 통해 차의 절댓값을 구하고
// 차가 같을 경우 작은 수가 오름차순 정렬될 수 있도록함

import kotlin.math.abs

class Solution {
    fun solution(array: IntArray, n: Int): Int {
        return array
            .sortedWith(
                compareBy<Int> { abs(n - it) }.thenBy { it }
            )
            .first()
    }
}
