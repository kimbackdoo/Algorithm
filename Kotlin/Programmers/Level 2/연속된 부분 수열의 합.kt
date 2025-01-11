// 투 포인터 알고리즘
class Solution {
    fun solution(sequence: IntArray, k: Int): List<Int> {
        val answer = mutableListOf<Int>(0, sequence.lastIndex)
        
        var tmp = 0
        var right = 0
        for (i in sequence.indices) {
            while (tmp < k && right < sequence.size) {
                tmp += sequence[right]
                right += 1
            }
            
            val endIndex = right - 1
            if (tmp == k && answer[1] - answer[0] > endIndex - i) {
                answer[0] = i
                answer[1] = endIndex
            }
            
            tmp -= sequence[i]
        }
        
        return answer
    }
}