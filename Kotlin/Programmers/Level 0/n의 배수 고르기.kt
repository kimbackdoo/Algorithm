// numlist를 순회하면서 n의 배수인 것만 filtering
class Solution {
    fun solution(n: Int, numlist: IntArray): IntArray {
        return numlist.filter { it % n == 0 }.toIntArray()
    }
}
