// 주어진 array에서 제일 큰 수를 찾고, 해당 index 값을 list로 return 하면 됨
class Solution {
    fun solution(array: IntArray): IntArray {
        val max = array.maxOf { it }
        val index = array.indexOf(max)
        return intArrayOf(max, index)
    }
}
