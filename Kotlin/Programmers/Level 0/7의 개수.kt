// 주어진 배열을 문자열로 변환 후 7의 개수 count

class Solution {
    fun solution(array: IntArray): Int {
        return array.joinToString("").count { it == '7' }
    }
}
