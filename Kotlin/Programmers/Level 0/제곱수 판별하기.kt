// n의 제곱근을 구하고, 그 제곱근의 제곱수와 n을 비교하여 답을 구함
// 코틀린에서는 제곱근의 값이 Double임
// 즉, 소수점이 있는데 부동소수점으로 인하여 오차가 발생할 수 있음
// 따라서 제곱근의 제곱수를 구할때, Double형을 Int로 바꾸고, Int를 Double로 바꾸어 계산함

import kotlin.math.*

class Solution {
    fun solution(n: Int): Int {
        val doubleN = n.toDouble()
        val result = sqrt(doubleN).toInt()
        return if (result.toDouble().pow(2) == doubleN) 1 else 2
    }
}
