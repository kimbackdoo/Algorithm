// 주어진 order를 문자열로 변환 후
// order를 순회하면서 해당 문자가 3, 6, 9에 포함되는지 counting
class Solution {
    fun solution(order: Int): Int {
        return order.toString().count { "369".contains(it) }
    }
}
