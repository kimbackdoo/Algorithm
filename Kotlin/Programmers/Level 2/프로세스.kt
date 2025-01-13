class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        val queue = ArrayDeque<Pair<Int, Int>>()
        priorities.forEachIndexed { index, priority -> queue += index to priority }
        
        var answer = 0
        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()
            if (queue.any { it.second > current.second }) {
                queue += current
                continue
            }
            
            answer += 1
            if (current.first == location) return answer
        }
        
        return answer
    }
}