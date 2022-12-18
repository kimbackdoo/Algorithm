// 주어진 n을 문자열로 변환 후 모두 더함
class Solution {
    fun solution(n: Int): Int {
        return n.toString().sumOf { it.digitToInt() }
    }
}
